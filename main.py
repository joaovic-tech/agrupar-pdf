import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_folder, output_filename):
    # Lista todos os arquivos no diretório de entrada
    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

    # Garante que os arquivos estejam ordenados corretamente
    pdf_files.sort()

    # Cria um objeto PdfMerger
    pdf_merger = PdfMerger()

    # Adiciona cada arquivo PDF ao objeto de mesclagem
    for pdf_file in pdf_files:
        pdf_merger.append(os.path.join(input_folder, pdf_file))

    # Salva o arquivo mesclado
    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Arquivos PDF mesclados com sucesso em {output_filename}')

# Substitua 'caminho\\para\\seus\\arquivos' pelo caminho real onde seus arquivos PDF estão
caminho_entrada = './'
nome_saida = 'arquivo_mesclado.pdf'

merge_pdfs(caminho_entrada, nome_saida)
