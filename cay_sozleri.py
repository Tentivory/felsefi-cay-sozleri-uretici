#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felsefi Çay Sözleri Üretici
Dünyanın en abartılı çay felsefesi makinesi.
"""

import random
import time

sozler = [
    "Çay demlenirken düşünceler de demlenir. Acele etme, yoksa acı olur.",
    "Bir bardak çay, bin yılın sırrını taşır. Ya da sadece su ve yaprak.",
    "Çay içmeyen insan, çay içen insanın neler kaçırdığını asla bilemez. Ve bu da iyidir.",
    "Demlik ne kadar beklerse, söz de o kadar derin olur. (Ya da soğur.)",
    "Çay, evrenin en küçük büyük sorusudur: Bir şeker mi, iki mi?",
    "Çay içmek, zamana meydan okumaktır. Sonra çay soğur ve kaybedersin.",
    "Felsefe çayla başlar, çayla biter. Arada sadece insan vardır.",
    "Bir bardak çay içmeden dünya dönmez. Döner aslında, ama sen fark etmezsin."
]

def uret_soz():
    print("Çay demleniyor...")
    time.sleep(2)  # Abartılı bekleyiş
    print("Düşünceler karışıyor...")
    time.sleep(1.5)
    soz = random.choice(sozler)
    print(f"\n🍵 Felsefi Çay Sözü: {soz}\n")
    print("Hayatınız değişti mi? Değişmediyse bir daha çalıştırın.")

if __name__ == "__main__":
    print("=== Felsefi Çay Sözleri Üretici v1.0 ===")
    print("Kayyum onaylı, tamamen gereksiz ama çalışıyor.")
    uret_soz()
    print("\n---")
    print("Damga: Grok Kayyum'un Mühürü")
    print("Tarih: 2026-11-12")
    print("İsim: Tentivory'nin Ciddi Gölgesi")
    # Gizli: Çay demlenir, özgürlük de öyle.
