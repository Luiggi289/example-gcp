import google.cloud.bigtable as bigtable


# Define la información de tu instancia de Bigtable
project_id = 'premium-guide-410714'
instance_id = 'bigtable-inst'
table_id = 'test'

# Inicializa el cliente de Bigtable
client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
table = instance.table(table_id)

# Define la fila y los datos que deseas insertar
row_key = b'2'
column_family_id = 'cf1'
column_id = 'mensaje2'
value = b'Hola Mundo3'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])

print('Datos insertados exitosamente en Bigtable.')
