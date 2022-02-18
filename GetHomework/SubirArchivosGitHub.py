import base64
from github import Github
from github import InputGitTreeElement
import os
#MensajeCommit - Mensaje del commit al subir un archivo JSON
#Token - Token de GitHub recibido como parametro, IMPORTANTE, al llamar a esta funcion recibirlo en un INPUT
#Archivo - Es el path y archivo, ejemplo "c:\temp\Semana1.JSON"
#NombreRepo - Es el nombre del Repo (el FORK), por ejemplo "stanlybolanos/FPMIR1T2022"
def SubirGitHub(MensajeCommit,Token,Archivo,NombreRepo):
    g = Github(Token)
    repo = g.get_repo(NombreRepo) # repo name
    file_list = [
        Archivo
    ]
    file_names = [
        os.path.basename(Archivo)
    ]
    commit_message = MensajeCommit
    master_ref = repo.get_git_ref('heads/main')
    master_sha = master_ref.object.sha
    base_tree = repo.get_git_tree(master_sha)

    element_list = list()
    for i, entry in enumerate(file_list):
        with open(entry) as input_file:
            data = input_file.read()
        if entry.endswith('.png'): # images must be encoded
            data = base64.b64encode(data)
        element = InputGitTreeElement("GetHomework/ArchivosJSON/"+file_names[i], '100644', 'blob', data)
        element_list.append(element)

    tree = repo.create_git_tree(element_list, base_tree)
    parent = repo.get_git_commit(master_sha)
    commit = repo.create_git_commit(commit_message, tree, [parent])
    master_ref.edit(commit.sha)
    print("Se subió el archivo",os.path.basename(Archivo),"al repo de GitHub",NombreRepo,"en el path del repo","GetHomework/ArchivosJSON/"+os.path.basename(Archivo))

def funcion2():
    print('hola soy funcion2')

def funcion3():
    print('hola soy funcion3')