# conversor de medida
dist_metro = float(input("Digite uma distância em metros: "))
km = dist_metro/1000
hm = dist_metro/100
dam = dist_metro/10
dm = dist_metro*10
cm = dist_metro*100
mm = dist_metro/1000
print(f"Em quilômetro: {km}km \nEm Hectômetro: {hm}hm \nEm Decâmetro: {dam}dam \nEm Decímetro: {dm}dm \nEm Centímetro: {cm}cm \nEm Milímetro: {mm}mm")