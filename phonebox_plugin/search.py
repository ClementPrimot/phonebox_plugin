from netbox.search import SearchIndex, register_search
from .models import Number, VoiceCircuit

@register_search
class PhoneNumberIndex(SearchIndex):
    model = Number
    fields = (
        ('number', 100),
        ('description', 5000)
    )

@register_search
class VoiceCircuitIndex(SearchIndex):
    model = VoiceCircuit
    fields = (
        ('name', 100),
        ('provider_circuit_id', 100),
        ('description', 5000)
    )