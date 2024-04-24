
### Bigtable





CREATE EXTERNAL TABLE premium-guide-410714.dep_raw.test_bigtable
OPTIONS (
  format = 'CLOUD_BIGTABLE',
  uris = ['https://googleapis.com/bigtable/projects/premium-guide-410714/instances/bigtable-inst/tables/test'],
  bigtable_options =
    """
    {
      columnFamilies: [
        {
          "familyId": "cf1",
          "type": "STRING",
          "encoding": "BINARY"
        },
        {
          "familyId": "cf2",
          "type": "STRING",
          "encoding": "BINARY"
        }
      ],
      readRowkeyAsString: true
    }
    """
);