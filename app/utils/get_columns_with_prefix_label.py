from sqlalchemy import Table


def get_columns_with_prefix_label(table_name: str, table: Table):
    col_with_labels = [col.label(f"{table_name}_{col.name}") for col in table.columns]

    return col_with_labels
