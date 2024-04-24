
import google.cloud.bigtable as bigtable
from google.cloud.bigtable.row_set import RowSet

# Configura tu proyecto y la instancia de Cloud Bigtable
project_id = "premium-guide-410714"
instance_id = "bigtable-inst"
table_id = "test"

client = bigtable.Client(project=project_id, admin=True)

instance = client.instance("bigtable-inst")
table = instance.table("test")

prefix = "phone#"
end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)

outputs = []
row_set = RowSet()
row_set.add_row_range_from_keys(prefix.encode("utf-8"), end_key.encode("utf-8"))

rows = table.read_rows(row_set=row_set)
for row in rows:
    output = "Rowkey: {}, os_build: {}".format(
        row.row_key.decode("utf-8"),
        row.cells["stats_summary"][b"os_build"][0].value.decode("utf-8"),
    )
    outputs.append(output)