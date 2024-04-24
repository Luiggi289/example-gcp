import google.cloud.bigtable as bigtable


# Define la información de tu instancia de Bigtable
project_id = 'premium-guide-410714'
instance_id = 'bigtable-inst'
table_id = 'clientes'

# Inicializa el cliente de Bigtable
client = bigtable.Client(project=project_id, admin=True)
instance = client.instance(instance_id)
table = instance.table(table_id)

# Define la fila y los datos que deseas insertar
row_key = b'1'
column_family_id = 'datos_cliente'
column_id = 'nombres'
value = b'Luis Morales'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])


# Define la fila y los datos que deseas insertar
row_key = b'1'
column_family_id = 'datos_cliente'
column_id = 'edad'
value = b'20'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])


# Define la fila y los datos que deseas insertar
row_key = b'1'
column_family_id = 'datos_cliente'
column_id = 'genero'
value = b'F'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])


# Define la fila y los datos que deseas insertar
row_key = b'1'
column_family_id = 'datos_adicionales'
column_id = 'saldo'
value = '1500'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])


# Define la fila y los datos que deseas insertar
row_key = b'1'
column_family_id = 'datos_adicionales'
column_id = 'score'
value = '0.7'

# Crea una fila de Bigtable
row = table.row(row_key)

# Agrega los datos a la fila
row.set_cell(column_family_id, column_id, value)

# Inserta la fila en la tabla
table.mutate_rows([row])




print('Datos insertados exitosamente en Bigtable.')
