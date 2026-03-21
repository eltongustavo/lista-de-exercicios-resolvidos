tamanho_arquivo = int(input('Digite quantos MB de tamanho o arquivo possui: '))
download_speed_seg = int(input('Digite qual sua velocidade de internet em Mbps: '))
download_time_seg = tamanho_arquivo / download_speed_seg
download_time_min = 0
while download_time_seg > 60:
    download_time_seg -= 60
    download_time_min += 1
print(f'Para baixar um arquivo de {tamanho_arquivo}MB com uma velocidade de {download_speed_seg}Mbps, levará cerca de'
      f' {download_time_min} minutos e {download_time_seg} segundos')
