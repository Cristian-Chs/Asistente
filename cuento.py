import random

def contar_cuento():
  cuento = [ 
    
    "El ratón y la biblioteca encantada. -- Había una vez un ratón llamado Tito que vivía en una biblioteca antigua. Cada noche, cuando todos se iban, los libros cobraban vida. Tito se hizo amigo de un atlas que viajaba por el mundo, una novela romántica que suspiraba todo el tiempo, y un diccionario que hablaba con palabras difíciles. Una noche, los libros le pidieron ayuda: alguien había robado la última página del cuento mágico. Tito se embarcó en una aventura entre estanterías, resolviendo acertijos y enfrentando al temido libro de terror. Al final, encontró la página escondida en un libro de recetas y devolvió la magia a la biblioteca."
  
    "La pluma que escribía sola. En un rincón olvidado de la biblioteca, había una pluma dorada que nadie usaba. Un día, una niña llamada Clara la encontró y al tocarla, la pluma comenzó a escribir sola. Cada noche, Clara dejaba la pluma sobre una hoja en blanco, y al despertar, encontraba cuentos maravillosos sobre dragones, sirenas y mundos invisibles. Pero un día, la pluma escribió: “Gracias por dejarme soñar contigo. Ahora debo volar.” Y desapareció. Clara siguió escribiendo, inspirada por la magia que una pluma le enseñó. "

    " El libro que no quería ser leído. En una estantería polvorienta vivía un libro llamado “El misterio del gusano tímido”. Cada vez que alguien intentaba abrirlo, las letras se escondían. Los lectores se frustraban y lo devolvían. Hasta que llegó Leo, un niño curioso que le habló al libro: “No te voy a juzgar, solo quiero conocerte.” Poco a poco, las letras regresaron y el libro se abrió. Dentro había una historia sobre un gusano que tenía miedo de brillar. Leo lo leyó con cariño, y desde entonces, el libro dejó de esconderse."
  ]

  return random.choice(cuento)