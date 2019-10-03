{
    "interactionModel": {
        "languageModel": {
            "invocationName": "youtube",
            "intents": [
                {
                    "name": "AMAZON.CancelIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.HelpIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.StopIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.PauseIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.ResumeIntent",
                    "samples": []
                },
                {
                    "name": "SearchIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Ponme {query}",
                        "Play {query}",
                        "Pon musica de {query}",
                        "Pon canciones de {query}",
                        "Pon temas de {query}",
                        "Pon tracks de {query}",
                        "Pon videos de {query}",
                        "Pon sonidos de {query}",
                        "Busca musica de {query}",
                        "Busca canciones de {query}",
                        "Busca temas de {query}",
                        "Busca tracks de {query}",
                        "Busca videos de {query}"
                    ]
                },
                {
                    "name": "PlayOneIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Pon la cancion {query}",
                        "Pon una cancion de {query}",
                        "Pon el tema {query}",
                        "Pon un tema de {query}",
                        "Pon el video {query}",
                        "Pon un video de {query}",
                        "Pon el track {query}",
                        "Pon un track de {query}"
                    ]
                },
                {
                    "name": "ShuffleIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Aleatorio canciones de {query}",                    
                        "Canciones en aleatorio de {query}",
                        "Canciones aleatorias de {query}",
                        "Temas en aleatorio de {query}",
                        "Temas aleatorios de {query}",
                        "Tracks en aleatorio de {query}",
                        "Tracks aleatorios de {query}",
                        "Videos en aleatorio de {query}",
                        "Videos aleatorios de {query}",
                        "Pon canciones en aleatorio de {query}",
                        "Pon canciones aleatorias de {query}",
                        "Pon musica en aleatorio de {query}",
                        "Pon musica aleatoria de {query}",
                        "Pon temas en aleatorio de {query}",
                        "Pon temas aleatorios de {query}",
                        "Pon tracks en aleatorio de {query}",
                        "Pon tracks aleatorios de {query}"
                    ]
                },
                {
                    "name": "PlaylistIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Pon playlist {query}",
                        "Pon lista {query}",
                        "Pon una playlist de {query}",
                        "Pon una lista de {query}",
                        "Pon la playlist {query}",
                        "Pon la lista {query}",
                        "Reproduce playlist de {query}"
                    ]
                },
                {
                    "name": "ShufflePlaylistIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Aleatorio playlist de {query}",
                        "Pon playlist aleatoria {query}",
                        "Pon lista aleatoria {query}",
                        "Pon una playlist aleatoria de {query}",
                        "Pon una lista aleatoria de {query}",
                        "Pon en aleatorio la lista {query}",
                        "Pon en aleatorio la playlist {query}",
                        "Haz una mezcla de la lista {query}",
                        "Haz un remix de la lista {query}",
                        "Lista aleatoria {query}",
                        "Aleatorio lista {query}",
                        "Mezcla la lista {query}",
                        "Remezcla la lista {query}",
                        "Playlist aleatoria {query}"
                    ]
                },
                {
                    "name": "SearchMyPlaylistsIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Pon mi lista {query}",
                        "Pon mi playlist {query}",
                        "Abre mi lista {query}",
                        "Reproduce mi lista {query}",
                        "Reproduce mi playlist {query}"
                    ]
                },
                {
                    "name": "NextPlaylistIntent",
                    "slots": [],
                    "samples": [
                        "Siguiente playlist",
                        "Siguiente lista"
                    ]
                },
                {
                    "name": "ShuffleMyPlaylistsIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Remueve mi lista {query}",
                        "Mezcla mi lista {query}",
                        "Remezcla mi lista {query}",
                        "Haz una mezcla de mi lista {query}",
                        "Haz una remix de mi lista {query}",
                        "Pon en aleatorio mi lista {query}"
                    ]
                },
                {
                    "name": "ChannelIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Pon el canal {query}",
                        "Abre el canal {query}",
                        "Reproduce el canal {query}"
                    ]
                },
                {
                    "name": "ShuffleChannelIntent",
                    "slots": [
                        {
                            "name": "query",
                            "type": "AMAZON.SearchQuery"
                        }
                    ],
                    "samples": [
                        "Pon en aleatorio el canal {query}",
                        "Pon en aleatorio el canal de {query}",
                        "Canal en aleatorio {query}",
                        "Canal aleatorio {query}"
                    ]
                },
                {
                    "name": "NowPlayingIntent",
                    "slots": [],
                    "samples": [
                        "Que esta sonando",
                        "Que suena",
                        "Quien es",
                        "Quien canta",
                        "Quien toca",
                        "Quien suena",
                        "Que video es",
                        "Que cancion es",
                        "Que cancion suena",
                        "Que es esto",
                        "Que se oye",
                        "Que se esta oyendo"
                    ]
                },
                {
                    "name": "PlayMoreLikeThisIntent",
                    "slots": [],
                    "samples": [
                        "Similar",
                        "Parecido",
                        "Pon mas de esto",
                        "Pon mas como esto",
                        "Pon mas videos como este",
                        "Pon mas videos parecidos a este",
                        "Pon mas musica como esta",
                        "Pon mas musica parecida a esta",
                        "Pon una cancion similar",
                        "Pon una cancion parecida",
                        "Pon una cancion como esta",
                        "Pon un tema similar",
                        "Pon un tema parecido",
                        "Pon un tema como este",
                        "Pon videos similares",
                        "Pon videos parecidos",
                        "Pon videos como este",
                        "Pon canciones similares",
                        "Pon canciones parecidas",
                        "Pon canciones como esta",
                        "Pon temas similares",
                        "Pon temas parecidos",
                        "Pon temas como este",
                        "Pon artistas similares",
                        "Pon artistas parecidos",
                        "Pon artistas como este",
                        "Pon musica parecida",
                        "Pon musica similar",
                        "Pon musica como esta",
                        "Busca mas de esto",
                        "Busca mas como esto",
                        "Busca mas videos como este",
                        "Busca mas videos parecidos a este",
                        "Busca mas musica como esta",
                        "Busca mas musica parecida a esta",
                        "Busca una cancion similar",
                        "Busca una cancion parecida",
                        "Busca una cancion como esta",
                        "Busca un tema similar",
                        "Busca un tema parecido",
                        "Busca un tema como este",
                        "Busca videos similares",
                        "Busca videos parecidos",
                        "Busca videos como este",
                        "Busca canciones similares",
                        "Busca canciones parecidas",
                        "Busca canciones como esta",
                        "Busca temas similares",
                        "Busca temas parecidos",
                        "Busca temas como este",
                        "Busca artistas similares",
                        "Busca artistas parecidos",
                        "Busca artistas como este",
                        "Busca musica parecida",
                        "Busca musica similar",
                        "Busca musica como esta"
                    ]
                },
                {
                    "name": "AutoplayOnIntent",
                    "slots": [],
                    "samples": [
                        "Enciende autoplay",
                        "Enciende el autoplay"
                    ]
                },
                {
                    "name": "AutoplayOffIntent",
                    "slots": [],
                    "samples": [
                        "Apaga autoplay",
                        "Apaga el autoplay"
                    ]
                },
                {
                    "name": "SayTimestampIntent",
                    "slots": [],
                    "samples": [
                        "Que minuto es",
                        "Que minuto del video es",
                        "Que minuto de la cancion es",
                        "Cual es la marca de tiempo"
                    ]
                },
                {
                    "name": "SkipToIntent",
                    "slots": [
                        {
                            "name": "minutes",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "seconds",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "hours",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [    
                        "Hora {hours}",
                        "Minuto {minutes}",
                        "Segundo {seconds}",
                        "Minuto {minutes} segundo {seconds}",                        
                        "Hora {hours} minuto {minutes}",
                        "Hora {hours} minuto {minutes} segundo {seconds}",            
                        "Salta {minutes} {seconds}",
                        "Salta {hours} {minutes} {seconds}",
                        "Salta a la hora {hours}",
                        "Salta al minuto {minutes}",
                        "Salta al segundo {seconds}",
                        "Salta al minuto {minutes} y al segundo {seconds}",
                        "Salta a la hora {hours} y al minuto {minutes}",
                        "Salta a la hora {hours} al minuto {minutes} y al segundo {seconds}",
                        "Ve a {minutes} {seconds}",
                        "Ve a {hours} {minutes} {seconds}",
                        "Ve a la hora {hours}",
                        "Ve al minuto {minutes}",
                        "Ve al segundo {seconds}",
                        "Ve a la hora {hours} y al minuto {minutes}",
                        "Ve a la hora {hours} al minuto {minutes} y al segundo {seconds}"
                    ]
                },
                {
                    "name": "SkipForwardIntent",
                    "slots": [
                        {
                            "name": "minutes",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "seconds",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "hours",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Avanza {minutes} {seconds}",
                        "Avanza {hours} {minutes} {seconds}",
                        "Avanza {hours} hora",
                        "Avanza {hours} horas",
                        "Avanza {minutes} minuto",
                        "Avanza {minutes} minutos",
                        "Avanza {seconds} segundo",
                        "Avanza {seconds} segundos",
                        "Avanza {hours} hora y {minutes} minuto",
                        "Avanza {hours} hora y {minutes} minutos",
                        "Avanza {hours} horas y {minutes} minuto",
                        "Avanza {hours} horas y {minutes} minutos",
                        "Avanza {hours} hora {minutes} minuto y {seconds} segundo",
                        "Avanza {hours} hora {minutes} minuto y {seconds} segundos",
                        "Avanza {hours} hora {minutes} minutos y {seconds} segundos",
                        "Avanza {hours} horas {minutes} minuto y {seconds} segundo",
                        "Avanza {hours} horas {minutes} minuto y {seconds} segundos",
                        "Avanza {hours} horas {minutes} minutos y {seconds} segundos",
                        "Adelanta {minutes} {seconds}",
                        "Adelanta {hours} {minutes} {seconds}",
                        "Adelanta {hours} hora",
                        "Adelanta {hours} horas",
                        "Adelanta {minutes} minuto",
                        "Adelanta {minutes} minutos",
                        "Adelanta {seconds} segundo",
                        "Adelanta {seconds} segundos",
                        "Adelanta {hours} hora y {minutes} minuto",
                        "Adelanta {hours} hora y {minutes} minutos",
                        "Adelanta {hours} horas y {minutes} minuto",
                        "Adelanta {hours} horas y {minutes} minutos",
                        "Adelanta {hours} hora {minutes} minuto y {seconds} segundo",
                        "Adelanta {hours} hora {minutes} minuto y {seconds} segundos",
                        "Adelanta {hours} hora {minutes} minutos y {seconds} segundos",
                        "Adelanta {hours} horas {minutes} minuto y {seconds} segundo",
                        "Adelanta {hours} horas {minutes} minuto y {seconds} segundos",
                        "Adelanta {hours} horas {minutes} minutos y {seconds} segundos",
                        "Salta {hours} hora",
                        "Salta {hours} horas",
                        "Salta {minutes} minuto",
                        "Salta {minutes} minutos",
                        "Salta {seconds} segundo",
                        "Salta {seconds} segundos",
                        "Salta {hours} hora y {minutes} minuto",
                        "Salta {hours} hora y {minutes} minutos",
                        "Salta {hours} horas y {minutes} minuto",
                        "Salta {hours} horas y {minutes} minutos",
                        "Salta {hours} hora {minutes} minuto y {seconds} segundo",
                        "Salta {hours} hora {minutes} minuto y {seconds} segundos",
                        "Salta {hours} hora {minutes} minutos y {seconds} segundos",
                        "Salta {hours} horas {minutes} minuto y {seconds} segundo",
                        "Salta {hours} horas {minutes} minuto y {seconds} segundos",
                        "Salta {hours} horas {minutes} minutos y {seconds} segundos"
                    ]
                },
                {
                    "name": "SkipBackwardIntent",
                    "slots": [
                        {
                            "name": "minutes",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "seconds",
                            "type": "AMAZON.NUMBER"
                        },
                        {
                            "name": "hours",
                            "type": "AMAZON.NUMBER"
                        }
                    ],
                    "samples": [
                        "Retrocede {minutes} {seconds}",
                        "Retrocede {hours} {minutes} {seconds}",
                        "Retrocede {hours} hora",
                        "Retrocede {hours} horas",
                        "Retrocede {minutes} minuto",
                        "Retrocede {minutes} minutos",
                        "Retrocede {seconds} segundo",
                        "Retrocede {seconds} segundos",
                        "Retrocede {hours} hora y {minutes} minuto",
                        "Retrocede {hours} hora y {minutes} minutos",
                        "Retrocede {hours} horas y {minutes} minuto",
                        "Retrocede {hours} horas y {minutes} minutos",
                        "Retrocede {hours} hora {minutes} minuto y {seconds} segundo",
                        "Retrocede {hours} hora {minutes} minuto y {seconds} segundos",
                        "Retrocede {hours} hora {minutes} minutos y {seconds} segundos",
                        "Retrocede {hours} horas {minutes} minuto y {seconds} segundo",
                        "Retrocede {hours} horas {minutes} minuto y {seconds} segundos",
                        "Retrocede {hours} horas {minutes} minutos y {seconds} segundos",
                        "Atrasa {minutes} {seconds}",
                        "Atrasa {hours} {minutes} {seconds}",
                        "Atrasa {hours} hora",
                        "Atrasa {hours} horas",
                        "Atrasa {minutes} minuto",
                        "Atrasa {minutes} minutos",
                        "Atrasa {seconds} segundo",
                        "Atrasa {seconds} segundos",
                        "Atrasa {hours} hora y {minutes} minuto",
                        "Atrasa {hours} hora y {minutes} minutos",
                        "Atrasa {hours} horas y {minutes} minuto",
                        "Atrasa {hours} horas y {minutes} minutos",
                        "Atrasa {hours} hora {minutes} minuto y {seconds} segundo",
                        "Atrasa {hours} hora {minutes} minuto y {seconds} segundos",
                        "Atrasa {hours} hora {minutes} minutos y {seconds} segundos",
                        "Atrasa {hours} horas {minutes} minuto y {seconds} segundo",
                        "Atrasa {hours} horas {minutes} minuto y {seconds} segundos",
                        "Atrasa {hours} horas {minutes} minutos y {seconds} segundos"
                    ]
                },                
                {
                    "name": "AMAZON.YesIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NoIntent",
                    "samples": []
                },
                {
                    "name": "AMAZON.NavigateHomeIntent",
                    "samples": []
                }
            ],
            "types": []
        }
    }
}
