from django.urls import reverse
from core.tests.test_api_abstract import ApiTests
from block.models import Block
from block.api.serializers.block_serializers import BlockSerializer


class BlockApiTests(ApiTests):

    url = reverse('block:block-list')
    Model = Block
    serializer_class = BlockSerializer

    def test_retrieve_object(self):

        self.Model.objects.create(
            status = False,
            merkle_root = '',
            block_hash = ''
        )

        objeto = self.Model.objects.all().order_by('-id')

    def test_create_object_successfull(self):

        payload = {
            "status": False,
            "merkle_root": '',
            "block_hash": ''
        }

    def test_create_object_invalid(self):
        payload = {'id': 'asd'}