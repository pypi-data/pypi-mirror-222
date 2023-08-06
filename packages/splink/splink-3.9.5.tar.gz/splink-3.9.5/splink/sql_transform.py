import sqlglot
import sqlglot.expressions as exp


def sqlglot_transform_sql(sql, func, dialect=None):
    syntax_tree = sqlglot.parse_one(sql, read=dialect)
    transformed_tree = syntax_tree.transform(func)
    return transformed_tree.sql(dialect)


def _add_l_or_r_to_identifier(node: exp.Expression):
    if not isinstance(node, exp.Identifier):
        return node

    p = node.parent
    if isinstance(p, (exp.Lambda, exp.Anonymous)):
        # node is the `x` in the lambda `x -> list_contains(r.name_list, x))`
        parent_table = ""
    else:
        parent_table = p.table

    if parent_table != "":
        l_r = "_" + parent_table
    else:
        l_r = ""
    node.args["this"] += l_r
    return node


def _remove_table_prefix(node):
    if isinstance(node, exp.Column):
        n = node.sql().replace(f"{node.table}.", "")
        return sqlglot.parse_one(n)
    return node


def move_l_r_table_prefix_to_column_suffix(blocking_rule):
    expression_tree = sqlglot.parse_one(blocking_rule, read=None)
    transformed_tree = expression_tree.transform(_add_l_or_r_to_identifier)
    transformed_tree = transformed_tree.transform(_remove_table_prefix)
    return transformed_tree.sql()
