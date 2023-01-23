import webbrowser
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the path to 
txt_path = os.path.join(current_dir, 'Lista.txt')

# Create the path to 
html_path = os.path.join(current_dir,'index.html')

# Create the path to 
script_path = os.path.join(current_dir,'script.js')


# Abrir o arquivo de texto com as URLs dos vídeos
with open(txt_path) as arquivo:
    urls_videos = [url.strip() for url in arquivo.readlines()]


# Cria o código HTML para a página
codigo_html = """
<html>
<head>
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<style>
/* Define a estrutura da tela dividida */
.video-container {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
}
/* Define o tamanho dos vídeos */
.video-container video {
    flex: 1;
    width: 50%;
    height: 50%;
}
</style>
</head>
<body>
<div class="video-container">
"""

# Gera o código HTML para cada vídeo
for i, url in enumerate(urls_videos):
    codigo_html += f'<video id="video{i+1}" controls></video>'

codigo_html += """
</div>
<script src="script.js"></script>
</body>
</html>
"""

# Gera o código JavaScript para cada vídeo
codigo_javascript = ""
for i, url in enumerate(urls_videos):
    codigo_javascript += f'''
        var video{i+1} = document.getElementById("video{i+1}");
        var hls{i+1} = new Hls();
        hls{i+1}.loadSource("{url}");
        hls{i+1}.attachMedia(video{i+1});
        hls{i+1}.on(Hls.Events.MANIFEST_PARSED, function() {{
        video{i+1}.play();
        }});
    '''

# Escrevendo no arquivo HTML
with open((html_path ), "w") as arq_html:
    arq_html.write(codigo_html)

# Escrevendo no arquivo JavaScript
with open((script_path ), "w") as arq_js:
    arq_js.write(codigo_javascript)

# abre o arquivo HTML no navegador
webbrowser.open_new_tab(html_path)

#    Creado por JULIOFMENDES
#    V.4.2