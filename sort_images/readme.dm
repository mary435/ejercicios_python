Ordenar el árbol de archivos.

Escribí un programa que te permita ordenar las imágenes PNG de una carpeta.

Cuando encuentres archivos con extensión png los vas a procesar. En este caso procesar significa:
Leer la fecha que se encuentra codificada en los últimos 8 caracteres de su nombre en el formato AAAAMMDD (año en 4 dígitos, mes en 2 y día en 2).
Usar la fecha obtenida para setear la fecha de última modificación (y de último acceso si no usás Windows).
Cambiarle el nombre al archivo para que no tenga más esos dígitos (ni el guión bajo).
Mover el archivo a la carpeta destino.
Los archivos que no son png no los modifiques.
Borrá todas las subcarpetas del archivo de origen que hayan quedado vacías.
Observación: Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro el directorio a leer original 
y un directorio destino (que debería ser creado si no existe).


Sort the file tree.

I wrote a program that allows you to sort the PNG images in a folder.

When you find files with png extension you will process them. In this case process means:
Read the date that is encoded in the last 8 characters of your name in the format YYYYMMDD (year in 4 digits, month in 2 and day in 2).
Use the obtained date to set the date of last modification (and last access if you are not using Windows).
Rename the file so that it no longer has those digits (or the underscore).
Move the file to the destination folder.
Don't modify non-png files.
Delete all subfolders of the source file that have been left empty.
Remark: At the end, your script should be able to be executed from the command line receiving the original directory to read as a parameter
and a destination directory (which should be created if it doesn't exist).
