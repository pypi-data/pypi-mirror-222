from __future__ import annotations

from collections.abc import Callable
import inspect
import logging
import types

from mknodes import mktable
from mknodes.utils import classhelpers, helpers


logger = logging.getLogger(__name__)


class MkModuleTable(mktable.MkTable):
    """Class representing a formatted table containing information a module."""

    def __init__(
        self,
        module: types.ModuleType | str | tuple[str, ...],
        *,
        predicate: Callable | None = None,
        **kwargs,
    ):
        self.module = classhelpers.to_module(module, return_none=False)
        dicts = [
            self.get_row_for_module(submod)
            for _, submod in inspect.getmembers(self.module, inspect.ismodule)
            if (predicate is None or predicate(submod)) and "__" not in submod.__name__
        ]
        super().__init__(dicts, **kwargs)

    def get_row_for_module(self, module: types.ModuleType) -> dict[str, str]:
        return dict(
            Name=module.__name__,
            # helpers.link_for_class(submod, size=4, bold=True),
            Information=helpers.get_doc(
                module,
                fallback="*No docstrings defined.*",
                only_summary=True,
            ),
            Members=(
                helpers.to_html_list(module.__all__, make_link=True)
                if hasattr(module, "__all__")
                else ""
            ),
        )

    # def __repr__(self):
    #     return helpers.get_repr(self, module=self.module)

    @staticmethod
    def create_example_page(page):
        import mkdocstrings

        import mknodes

        node = MkModuleTable(module=mkdocstrings)
        page += node
        page += mknodes.MkCode(str(node), language="markdown", header="Markdown")


if __name__ == "__main__":
    table = MkModuleTable(module=helpers)
    print(table)
