from __future__ import annotations

import logging

from mknodes import mkcontainer, mknode
from mknodes.utils import helpers


logger = logging.getLogger(__name__)


class MkList(mkcontainer.MkContainer):
    """Node for showing a formatted list."""

    def __init__(
        self,
        items: list[str | mknode.MkNode] | None = None,
        *,
        ordered: bool = False,
        shorten_after: int | None = None,
        as_links: bool = False,
        header: str = "",
    ):
        """Constructor.

        Arguments:
            items: Items to show as a list
            ordered: whether the list should be numbered
            shorten_after: will clip the list after n items and append a "..."
            as_links: will convert the label to links which will get replaced by plugin
            header: Section header
        """
        # if as_links:
        #     items = [link.Link(i) for i in items]
        super().__init__(content=items, header=header)
        self.ordered = ordered
        self.shorten_after = shorten_after
        self.as_links = as_links

    def __str__(self):
        return self.to_markdown()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return helpers.get_repr(
            self,
            items=self.items,
            shorten_after=self.shorten_after,
            as_links=self.as_links,
        )

    @staticmethod
    def create_example_page(page):
        import mknodes

        list_1 = MkList(items=["Item 1", "Item 2", "Item 3"], header="Regular")
        # list can also have a max length. they will get shortened with a "..." entry.
        list_2 = MkList(items=["Item"] * 6, shorten_after=3, header="Shortened")
        # They can also be ordered.
        list_3 = MkList(
            items=["Item 1", "Item 2", "Item 3"],
            ordered=True,
            header="Ordered",
        )
        page += list_1
        page += list_2
        page += list_3
        code = "\n".join(str(i) for i in [list_1, list_2, list_3])
        page += mknodes.MkCode(code, language="markdown", header="Markdown")

    def _prep(self, item) -> str:
        return helpers.linked(item) if self.as_links else str(item)

    def _to_markdown(self) -> str:
        if not self.items:
            return ""
        prefix = "1." if self.ordered else "*"
        lines = [f"  {prefix} {self._prep(i)}" for i in self.items[: self.shorten_after]]
        if self.shorten_after and len(self.items) > self.shorten_after:
            lines.append(f"  {prefix} ...")
        return "\n".join(lines) + "\n"

    def to_html(self) -> str:
        """Formats list in html as one single line.

        Can be useful for including in Tables.
        """
        if not self.items:
            return ""
        tag_name = "ol" if self.ordered else "ul"
        items = [f"<li>{self._prep(i)}</li>" for i in self.items[: self.shorten_after]]
        item_str = "".join(items)
        if self.shorten_after and len(self.items) > self.shorten_after:
            item_str += "<li>...</li>"
        return f"<{tag_name}>{item_str}</{tag_name}>"


if __name__ == "__main__":
    section = MkList(["a", "b"], header="test")
    print(section.to_html())
