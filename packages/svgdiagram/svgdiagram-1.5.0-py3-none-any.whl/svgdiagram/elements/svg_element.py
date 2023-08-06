INF_CON = float('inf')


class SvgElement:
    def __init__(self, tag_name, attributes=None, children=None) -> None:
        self.tag_name = tag_name
        self.attributes = attributes if attributes else {}

        if not isinstance(children, list) and children:
            children = [children]

        self.children = children if children else []

    @property
    def bounds(self):
        """Bounds provided by [xmin, xmax, ymin, ymax]"""
        raise NotImplementedError

    @property
    def size(self):
        bnds = self.bounds
        return bnds[1]-bnds[0], bnds[3]-bnds[2]

    @property
    def defs(self):
        childs = self.children
        childs = list(filter(lambda x: isinstance(x, SvgElement), childs))
        list_of_lists = list(map(lambda x: x.defs, childs))
        return [item for sublist in list_of_lists for item in sublist]

    def _render(self, doc, tag, text, debug, inject_pre_children=None):
        kv_attribs = [(k, v) for k, v in self.attributes.items()]

        children = self.children
        if inject_pre_children:
            children = inject_pre_children + children

        with tag(self.tag_name, *kv_attribs):
            for child in children:
                if isinstance(child, str):
                    text(child)
                else:
                    child._render(doc, tag, text, debug)

    def _layout(self, x_con_min, x_con_max, y_con_min, y_con_max):
        """layout before writing svg file

        By default
        - layouting is unconstraint
        - every element layouts itself

        Elements may
        - set position child elements
        - request width and height of the child elements
        - apply constraints to the with and height of child elements
        """
        assert x_con_min == -INF_CON
        assert x_con_max == INF_CON
        assert y_con_min == -INF_CON
        assert y_con_max == INF_CON

        for child in self.children:
            if not isinstance(child, str):
                child._layout(x_con_min, x_con_max, y_con_min, y_con_max)

    def insert_child(self, index, child):
        self.children.insert(index, child)

    def append_child(self, child):
        self.children.append(child)

    def extend_childs(self, childs):
        self.children.extend(childs)
