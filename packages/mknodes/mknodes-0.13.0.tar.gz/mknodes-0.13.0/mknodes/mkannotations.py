from __future__ import annotations

from collections.abc import Mapping
import logging

from mknodes import mkcontainer, mknode, mktext
from mknodes.utils import helpers


logger = logging.getLogger(__name__)


class MkAnnotation(mkcontainer.MkContainer):
    """Represents a single annotation. It gets managed by an MkAnnotations node."""

    def __init__(self, num: int, item: str | mknode.MkNode, **kwargs):
        super().__init__(items=[item], **kwargs)
        self.num = num

    def __repr__(self):
        return helpers.get_repr(self, num=self.num, item=self.items[0])

    def _to_markdown(self) -> str:
        item_str = "\n\n".join(i.to_markdown() for i in self.items)
        lines = item_str.split("\n")
        space = (3 - len(str(self.num))) * " "
        result = [f"{self.num}.{space}{lines[0]}"]
        result.extend(f"    {i}" for i in lines[1:])
        return "\n".join(result) + "\n"


class MkAnnotations(mkcontainer.MkContainer):
    """Node containing a list of MkAnnotations."""

    items: list[MkAnnotation]

    def __init__(
        self,
        annotations: Mapping[int, str | mknode.MkNode]
        | list[MkAnnotation]
        | list[str]
        | None = None,
        header: str = "",
        **kwargs,
    ):
        match annotations:
            case None:
                items = []
            case list():
                items = [
                    (
                        ann
                        if isinstance(ann, MkAnnotation)
                        else MkAnnotation(i, ann)  # type: ignore
                    )
                    for i, ann in enumerate(annotations, start=1)
                ]
            case Mapping():
                items = [
                    MkAnnotation(
                        k,
                        item=mktext.MkText(v) if isinstance(v, str) else v,
                    )
                    for k, v in annotations.items()
                ]
        for item in items:
            item.parent_item = self
        super().__init__(items=items, header=header, **kwargs)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, item: int):
        for annotation in self.items:
            if annotation.num == item:
                return annotation
        raise IndexError(item)

    def __contains__(self, annotation: int | MkAnnotation) -> bool:
        match annotation:
            case MkAnnotation():
                return annotation in self.items
            case int():
                return any(i.num == annotation for i in self.items)
            case _:
                raise TypeError(annotation)

    def _get_annotation_pos(self, num: int) -> int:
        item = next(i for i in self.items if i.num == num)
        return self.items.index(item)

    def __setitem__(self, index: int, value: mknode.MkNode | str):
        match value:
            case str():
                item = mktext.MkText(value)
                annotation = MkAnnotation(index, item=item)
            case MkAnnotation():
                annotation = value
            case mknode.MkNode():
                annotation = MkAnnotation(index, item=value)
        if index in self:
            pos = self._get_annotation_pos(index)
            self.items[pos] = annotation
        else:
            self.items.append(annotation)

    @staticmethod
    def create_example_page(page):
        import mknodes

        page += mknodes.MkCode.for_object(
            MkAnnotations.create_example_page,
            extract_body=True,
        )
        node = MkAnnotations()
        page += "The MkAnnotations node aggregates annotations."
        node[1] = r"Annotations are numbered and can be set via \__setitem__."  # (1)
        node[2] = mknodes.MkAdmonition("They can also contain other Markdown.")  # (2)
        page += node
        page += mknodes.MkCode(str(node), language="markdown", header="Markdown")

    def _to_markdown(self) -> str:
        return "".join(str(i) for i in self.items) if self.items else ""


if __name__ == "__main__":
    import mknodes

    # ann = MkAnnotation(1, "test")
    # print(ann)
    page = mknodes.MkPage()
    MkAnnotations.create_example_page(page)
    print(page)
