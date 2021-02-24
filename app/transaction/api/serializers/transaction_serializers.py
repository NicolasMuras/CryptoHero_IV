import hashlib
from django.db.models import Count
from rest_framework import serializers

from transaction.models import Transaction
from block.models import Block

#############################################[  GLOBALS  ]############################################

def objects_to_hash256(objects):

    # Concatenamos los objetos en nuestro dict.
    chained_data = ''.join(str(x) for x in objects.values())
    print('unhashed: {}'.format(str(chained_data)))

    # Necesitamos codificar en 'utf-8' antes de hacer el hash.
    chained_data = chained_data.encode('utf-8')

    # Creamos un objeto hashlib para almacenar nuestros datos encriptados.
    crypter = hashlib.sha256()

    # Almacenamos los datos de 'chained_data' en el 'crypter'.
    crypter.update(chained_data)

    # Encriptamos los datos con la funcion 'hexdigest()'.
    encrypted_data = crypter.hexdigest()
    print('hashed: {}'.format(encrypted_data))

    return encrypted_data

######################################################################################################


class TransactionSerializer(serializers.ModelSerializer):

    sender = serializers.CharField(max_length = 255)
    receiver = serializers.CharField(max_length = 255)
    amount = serializers.FloatField()
    timestamp = serializers.IntegerField()

    class Meta:
        model = Transaction
        fields = ('id', 'sender', 'receiver', 'amount', 'timestamp')
        read_only_fields = ('id',)

    def create(self, validated_data):

        # Almacenamos los datos encriptados en su field.
        validated_data['txhash'] = objects_to_hash256(validated_data)

        # Consultamos el id del ultimo block creado.
        quantity = Transaction.objects.annotate(number_of_entries = Count('id'))

        try:
            entries = quantity[0].number_of_entries
            print('Entries: {}'.format(entries))
        except Exception:
            entries = 0
            print('Entries: 0')

        # Comprobamos si el block tiene espacio libre.
        if entries % 4 == 0 and entries > 3:

            ################################################[ prev_hash ]################################################

            # Commit al bloque actual (lo guardamos en la blockchain).
            crypter_block = hashlib.sha256()
            
            # Conseguir el 'prev_hash' del block anterior.
            # Conseguir el 'id' del ultimo block.
            # Conseguir el 'merkle_tree' del ultimo block.

            # Obtenemos el Id del block actual y su prev_hash.
            quantity = Block.objects.annotate(number_of_entries=Count('id'))

            try:
                last_id = quantity[0].number_of_entries
                print('Entries: {}'.format(entries))
            except Exception:
                last_id = 0
                print('Entries: 0')

            prev_hash = Block.objects.get(id__exact = last_id).filter('block_hash')

            ###############################################[ merkle_root ]###############################################

            # Actualizamos el 'merkle_root' en el block.
            merkle_root = ''
            # Tomar las transacciones del bloque y devolver los txhash.
            transactions_in_block = entries % 4

            # Restar el numero de 'transactions_in_block' a la cantidad total de 'transactions' para obtener el primer id.
            entry_id = entries - transactions_in_block + 1

            # Concatenar los hash de a pares, volver a hacer hash en cada nodo para obtener el 'merkle_root'
            for i in range(transactions_in_block):

                # Obtener el attributo 'txhash' de la 'transaction' utilizando su id.
                txhash_value = Transaction.objects.get('txhash').filter(id = entry_id + i)
                print('txhash_value: {}'.format(txhash_value))
                # Concatenar pares y hacer hash.

                merkle_root.join(txhash_value)
                print(merkle_root)

            crypter_block.update(('{}{}{}'.format(prev_hash, last_id, merkle_root)).encode('utf-8'))

            prev_hash = crypter_block.hexdigest()

            ################################################[ commit ]###################################################

            data_block = {'status': True, 'merkle_root': merkle_root, 'block_hash': prev_hash}

            # Actualizamos el block, añadiendo una 'transaction'.
            Block.objects.update(**data_block)

            # Establecemos el identificador del bloque al campo 'block' de nuestra 'transaction'.
            block = Block.objects.get(id = last_id - 1)
            validated_data['block'] = block

            ################################################[ create ]###################################################

            # Creamos un nuevo block.
            data_block = {'status': False, 'merkle_root': '', 'block_hash': prev_hash}
            block = Block.objects.create(**data_block)

            # Establecemos el identificador del bloque al campo 'block' de nuestra 'transaction'.
            validated_data['block'] = block

        elif entries > 0:

            ###############################################[ merkle_root ]###############################################

            # Actualizamos el 'merkle_root' en el block.
            merkle_root = ''
            # Tomar las transacciones del bloque y devolver los txhash.
            transactions_in_block = entries % 4

            # Restar el numero de 'transactions_in_block' a la cantidad total de 'transactions' para obtener el primer id.
            entry_id = entries - transactions_in_block + 1
            print('entry_id: {}'.format(entry_id))
            # Concatenar los hash de a pares, volver a hacer hash en cada nodo para obtener el 'merkle_root'
            for i in range(transactions_in_block):
                print('i: {}'.format(i))

                # Obtener el attributo 'txhash' de la 'transaction' utilizando su id.

                field_value = getattr(Transaction.objects.get(id = entry_id + i), 'txhash')

                print('txhash_value: {}'.format(field_value))

                # Concatenar pares y hacer hash.
                if (i % 2 == 0) and (i != 0):
                    # Hash 'merkle_root'.
                    pass

                merkle_root = merkle_root.join(field_value)
                print('merkle_root: {}'.format(merkle_root))

            # Obtenemos el Id del block actual.
            quantity = Block.objects.annotate(number_of_entries = Count('id'))

            try:
                last_id = quantity[0].number_of_entries
                print('Entries: {}'.format(entries))
            except Exception:
                last_id = 0
                print('Entries: 0')

            # Obtenemos el hash del block actual.
            prev_hash = getattr(Block.objects.get(id = last_id), 'block_hash')


            data_block = {'status': False, 'merkle_root': merkle_root, 'block_hash': prev_hash}
            Block.objects.update(**data_block)

            
            # Establecemos el identificador del bloque al campo 'block' de nuestra 'transaction'.
            block = Block.objects.get(id = last_id)
            validated_data['block'] = block

        elif entries == 0:
            # Coinbase block.
            data_block = {'status': False, 'merkle_root': '', 'block_hash': ''}
            
            block = Block.objects.create(**data_block)

            # Establecemos el identificador del bloque al campo 'block' de nuestra 'transaction'.
            validated_data['block'] = block

        # Creamos la 'transaction'.
        transaction = Transaction.objects.create(**validated_data)
        transaction.save()
        return transaction

class DetailTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'