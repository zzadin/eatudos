larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area = larg * alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'
       .format(larg, alt, area))
tinta = area / 2
print ('Para pintar essa parede você precisa de {:.2f}L de tinta'
       .format(tinta))
