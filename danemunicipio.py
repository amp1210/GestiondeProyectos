import frmPrincipal

def denesmunicipio(municipio):
    mtzMunicipios = [["Caceres","120"],["Caucasia","154"],["El Bagre","250"],["Nechi","495"],["Taraza","790"],["Zaragoza","895"],
                    ["Caracoli","142"],["Maceo","425"],["Puerto Berrio","579"],["Puerto Nare","585"],["Puerto Triunfo","591"],
                    ["Yondo","893"],["Amalfi","031"],["Anori","040"],["Cisneros","190"],["Remedios","604"],["San Roque","670"],
                    ["Santo Domingo","690"],["Segovia","736"],["Vegachi","858"],["Yali","885"],["Yolombo","890"],["Angostura","038"],
                    ["Belmira","086"],["Briceno","107"],["Campamento","134"],["Carolina","150"],["Don Matias","237"],["Entrerrios","264"],
                    ["Gomez Plata","310"],["Guadalupe","315"],["Ituango","361"],["San Andres","647"],["San Jose De La Montana","658"],
                    ["San Pedro","664"],["Santa Rosa De Osos","686"],["Toledo","819"],["Valdivia","854"],["Yarumal","887"],["Abriaqui","004"],
                    ["Anza","044"],["Armenia","059"],["Buritica","113"],["Canasgordas","138"],["Dabeiba","234"],["Ebejico","240"],["Frontino","284"],
                    ["Giraldo","306"],["Heliconia","347"],["Liborina","411"],["Olaya","501"],["Peque","543"],["Sabanalarga","628"],
                    ["San Jeronimo","656"],["Santafe De Antioquia","042"],["Sopetran","761"],["Uramita","842"],["Abejorral","002"],
                    ["Alejandria","021"],["Argelia","055"],["Carmen De Viboral","148"],["Cocorna","197"],["Concepcion","206"],
                    ["Granada","313"],["Guarne","318"],["Guatape","321"],["La Ceja","376"],["La Union","400"],["Marinilla","440"],
                    ["Narino","483"],["Penol","541"],["Retiro","607"],["Rionegro","615"],["San Carlos","649"],["San Francisco","652"],
                    ["San Luis","660"],["San Rafael","667"],["San Vicente","674"],["Santuario","697"],["Sonson","756"],["Amaga","030"],
                    ["Andes","034"],["Angelopolis","036"],["Betania","091"],["Betulia","093"],["Caicedo","125"],["Caramanta","145"],
                    ["Ciudad Bolivar","101"],["Concordia","209"],["Fredonia","282"],["Hispania","353"],["Jardin","364"],["Jerico","368"],
                    ["La Pintada","390"],["Montebello","467"],["Pueblorrico","576"],["Salgar","642"],["Santa Barbara","679"],["Tamesis","789"],
                    ["Tarso","792"],["Titiribi","809"],["Urrao","847"],["Valparaiso","856"],["Venecia","861"],["Apartado","045"],
                    ["Arboletes","051"],["Carepa","147"],["Chigorodo","172"],["Murindo","475"],["Mutata","480"],["Necocli","490"],
                    ["San Juan De Uraba","659"],["San Pedro De Uraba","665"],["Turbo","837"],["Vigia Del Fuerte","873"],["Barbosa","079"],
                    ["Bello","088"],["Caldas","129"],["Copacabana","212"],["Envigado","266"],["Girardota","308"],["Itagui","360"],
                    ["La Estrella","380"],["Medellin","001"],["Sabaneta","631"]]
    
    for i in range(len(mtzMunicipios)):
        if municipio == mtzMunicipios[i][0]:
            return(mtzMunicipios[i][1])
    return("No Encontrado")