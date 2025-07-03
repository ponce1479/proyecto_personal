from django.shortcuts import render, HttpResponse

html_base = """

    
"""

# Create your views here.(
def home(request):
    return render(request,"core/home.html")
    # html_response = "<h1>Mi Sitio Web</h1>"
    # for i in range(10):
    #     html_response += f"<h2>Portada {i}</h2>"
    # return HttpResponse(html_response)
    
    #  return HttpResponse(html_base+"""
    #                      <h2>Portada</h2>
                         
    #                      <p>Bienvenido a mi sitio web. Aquí encontrarás información sobre mí y mis proyectos.</p>
    #                      <p>Esta es una página de ejemplo creada con Django.</p>
    #                      <p>¡Espero que te guste!</p>
    #                      <footer>
    #                          <p>&copy; 2025 Mi Sitio Web</p>
    #                          </footer>""")
 
def about(request):
    return render(request,"core/about.html")
        # return HttpResponse(html_base + """
        #                     <h2>Acerca de</h2>
        #                     <p>Esta es la página de acerca de mi sitio web.</p>
        #                     <p>Aquí puedes encontrar información sobre mí y mis proyectos.</p>
        #                        <footer>
        #                      <p>&copy; 2025 Mi Sitio Web</p>
        #                      </footer>""")
        
# def portfolio(request):
#     return render(request,"core/portfolio.html")
        # return HttpResponse(html_base + """
        #                     <h2>Portafolio</h2>
        #                     <p>Esta es la página de portafolio de mi sitio web.</p>
        #                     <p>Aquí puedes encontrar ejemplos de mi trabajo y proyectos anteriores.</p>
        #                        <footer>
        #                      <p>&copy; 2025 Mi Sitio Web</p>
        #                      </footer>""")

def contact(request):
    return render(request,"core/contact.html")
        # return HttpResponse(html_base + """
        #                     <h2>Contacto</h2>
        #                     <p>Esta es la página de contacto de mi sitio web.</p>
        #                     <p>Puedes encontrar información sobre cómo comunicarte conmigo.</p>
        #                        <footer>
        #                      <p>&copy; 2025 Mi Sitio Web</p>
        #                      </footer>""")

    