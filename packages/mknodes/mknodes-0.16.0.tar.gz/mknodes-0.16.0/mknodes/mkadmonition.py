from __future__ import annotations

import logging
import textwrap

from typing import Any, Literal

from mknodes import mkcontainer, mknode
from mknodes.utils import helpers


logger = logging.getLogger(__name__)

AdmonitionTypeStr = Literal[
    "node",
    "abstract",
    "info",
    "tip",
    "success",
    "question",
    "warning",
    "failure",
    "danger",
    "bug",
    "example",
    "quote",
]


class MkAdmonition(mkcontainer.MkContainer):
    """Admonition info box."""

    def __init__(
        self,
        content: str | list | mknode.MkNode,
        *,
        typ: AdmonitionTypeStr = "info",
        title: str | None = None,
        collapsible: bool = False,
        expanded: bool = False,
        inline: Literal["left", "right"] | None = None,
        **kwargs: Any,
    ):
        """Constructor.

        Arguments:
            content: Admonition content
            typ: Admonition type
            title: Optional Admonition title
            collapsible: Whether Admontion can get collapsed by user
            expanded: Initial state if collapsible is set
            inline: Whether admonition should rendered as inline block
            kwargs: Keyword arguments passed to parent
        """
        super().__init__(content=content, **kwargs)
        self.typ = typ
        self.title = title
        self.collapsible = collapsible
        self.inline = inline
        self.expanded = expanded

    def __repr__(self):
        return helpers.get_repr(self, content=self.items, typ=self.typ, title=self.title)

    def _to_markdown(self) -> str:
        if not self.items and not self.title:
            return ""
        block_start = "???" if self.collapsible else "!!!"
        if self.collapsible and self.expanded:
            block_start += "+"
        if self.inline:
            inline_label = " inline" if self.inline == "left" else " inline end"
        else:
            inline_label = ""
        title = f' "{self.title}"' if self.title else ""
        text = textwrap.indent("\n".join(str(i) for i in self.items), "    ")
        return f"{block_start} {self.typ}{inline_label}{title}\n{text}\n"

    @staticmethod
    def create_example_page(page):
        import mknodes

        node = mknodes.MkAdmonition("The MkAdmonition node is used to show Admonitions.")
        page += node
        page += "This is the resulting code:"
        page += mknodes.MkCode(str(node), language="markdown")
        for typ in [
            "node",
            "abstract",
            "info",
            "tip",
            "success",
            "question",
            "warning",
            "failure",
            "danger",
            "bug",
            "example",
            "quote",
        ]:
            admonition = mknodes.MkAdmonition(
                typ=typ,
                content=f"This is type {typ}",
                title=typ,
            )
            page += admonition
            page += mknodes.MkCode(str(admonition), language="markdown")
        admonition = mknodes.MkAdmonition(
            content="Admonitions can also be collapsible",
            collapsible=True,
            title="Expand me!",
        )
        page += admonition
        page += mknodes.MkCode(str(admonition), language="markdown")

        admonition = mknodes.MkAdmonition(
            content="The initial state can also changed for collapsible admonitions.",
            collapsible=True,
            expanded=True,
            title="Collapse me!",
        )
        page += admonition
        page += mknodes.MkCode(str(admonition), language="markdown")
        admonition = mknodes.MkAdmonition(
            content="Inlined.",
            inline="left",
            title="Inlined.",
        )
        page += admonition
        page += mknodes.MkCode(str(admonition), language="markdown")


if __name__ == "__main__":
    admonition = MkAdmonition("")
    print(admonition)
