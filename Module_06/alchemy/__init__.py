"""
alchemy — Laboratorio alquímico.

Gateway del paquete. Controla qué funciones quedan expuestas
como interfaz pública del módulo 'alchemy'.
"""

from .elements import create_air  # noqa: F401
# create_earth is intentionally out of public access

from .potions import healing_potion, strength_potion  # noqa: F401
heal = healing_potion

from .transmutation.recipes import lead_to_gold  # noqa: F401, E402
