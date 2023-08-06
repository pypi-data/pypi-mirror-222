from __future__ import annotations

from collections.abc import Mapping
import logging

from mknodes import mkcontainer, mknode, mktabs, mktext
from mknodes.utils import helpers


logger = logging.getLogger(__name__)


class MkTabContainer(mkcontainer.MkContainer):
    items: list[mktabs.MkTab | mktabs.MkTabBlock]
    Tab: type[mktabs.MkTab] | type[mktabs.MkTabBlock]

    def __init__(
        self,
        tabs: Mapping[str, str | mknode.MkNode] | list[mktabs.MkTab],
        *,
        header: str = "",
        select_tab: int | str | None = None,
        **kwargs,
    ):
        """Constructor.

        Arguments:
            tabs: Tab data
            header: Section header
            select_tab: Tab which should be selected initially
            kwargs: Keyword arguments passed to parent
        """
        if isinstance(tabs, list):
            items = tabs
        else:
            items = [
                self.Tab(
                    title=k,
                    content=mktext.MkText(v) if isinstance(v, str) else v,
                )
                for k, v in tabs.items()
            ]
        for tab in items:
            tab.parent_item = self
        match select_tab:
            case int():
                items[select_tab].select = True
            case str():
                pos = self._get_tab_pos(select_tab)
                items[pos].select = True
        super().__init__(content=items, header=header, **kwargs)

    def __getitem__(self, item: int | str) -> mktabs.MkTab | mktabs.MkTabBlock:
        match item:
            case int():
                return self.items[item]
            case str():
                for tab in self.items:
                    if tab.title == item:
                        return tab
                raise IndexError(item)
            case _:
                raise TypeError(item)

    def __contains__(self, tab: str | mktabs.MkTab | mktabs.MkTabBlock) -> bool:
        match tab:
            case mktabs.MkTab() | mktabs.MkTabBlock():
                return tab in self.items
            case str():
                return any(i.title == tab for i in self.items)
            case _:
                raise TypeError(tab)

    def _get_tab_pos(self, tab_title: str) -> int:
        item = next(i for i in self.items if i.title == tab_title)
        return self.items.index(item)

    def __setitem__(self, index: str, value: mktabs.MkTab | mktabs.MkTabBlock | str):
        match value:
            case str():
                item = mktext.MkText(value)
                tab = self.Tab(index, content=item)
            case mktabs.MkTab() | mktabs.MkTabBlock():
                tab = value
            case mknode.MkNode():
                tab = self.Tab(index, content=value)
        if index in self:
            pos = self._get_tab_pos(index)
            self.items[pos] = tab
        else:
            self.items.append(tab)

    def __repr__(self):
        return helpers.get_repr(self, tabs=self.items)

    def to_dict(self):
        return {tab.title: str(tab) for tab in self.items}

    def _to_markdown(self) -> str:
        return "\n".join(str(i) for i in self.items)


class MkTabbed(MkTabContainer):
    """pymdownx-based Tab block."""

    items: list[mktabs.MkTab]
    REQUIRED_EXTENSIONS = "pymdownx.tabbed"
    Tab = mktabs.MkTab

    @staticmethod
    def create_example_page(page):
        import mknodes

        # this node is basically a container and manager for MkTabs nodes.
        node = MkTabbed(tabs={"Tab 1": "Some markdown", "Tab 2": "Other Markdown"})
        page += node
        page += mknodes.MkCode(str(node), language="markdown", header="Markdown")


class MkTabbedBlocks(MkTabContainer):
    """New blocks-based Tab block."""

    items: list[mktabs.MkTabBlock]
    REQUIRED_EXTENSIONS = "pymdownx.blocks.tab"
    Tab = mktabs.MkTabBlock

    @staticmethod
    def create_example_page(page):
        import mknodes

        # this one is basically the same as MkTabbed,
        # but based on new pymdownx block syntax.
        # i think it is not supported by Material for MkDocs yet.
        node = MkTabbedBlocks(tabs={"Tab 1": "Some markdown", "Tab 2": "Other Markdown"})
        page += node
        page += mknodes.MkCode(str(node), language="markdown", header="Markdown")

    def _to_markdown(self) -> str:
        if not self.items:
            return ""
        self.items[0].new = True
        return "\n".join(str(i) for i in self.items)


if __name__ == "__main__":
    tabs = dict(Tab1="Some text", Tab2="Another text")
    tabblock = MkTabbedBlocks(tabs)
    print(tabblock)
