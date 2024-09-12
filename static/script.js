document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('parenteForm');
    const parentesList = document.getElementById('parentesList');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {
            nome: formData.get('nome'),
            pais: formData.get('pais').split(',').map(item => item.trim()),
            filhos: formData.get('filhos').split(',').map(item => item.trim()),
            irmaos: formData.get('irmaos').split(',').map(item => item.trim()),
            conjuge: formData.get('conjuge')
        };

        fetch('/parentes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            form.reset();
            carregarParentes();
        })
        .catch(error => console.error('Error:', error));
    });

    function carregarParentes() {
        fetch('/parentes')
        .then(response => response.json())
        .then(data => {
            ajustaParentes(data);
            parentesList.innerHTML = '';
            data.forEach(parente => {
                const li = document.createElement('li');
                li.textContent = `Id: ${parente['id']}, Nome: ${parente['nome']}, Pais: ${parente['pais']}, Filhos: ${parente['filhos']}, Irmãos: ${parente['irmaos']}, Cônjuge: ${parente['conjuge']}`;
                parentesList.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));
    }

    function ajustaParentes(parentes) {
        // Cria um mapa de IDs para nomes
        const idParaNome = {};
        parentes.forEach(parente => {
            idParaNome[parente[0]] = parente[1];
        });

        // Substitui os IDs pelos nomes correspondentes
        parentes.forEach(parente => {
            parente[2] = Array.isArray(parente[2]) ? parente[2].map(id => idParaNome[id] || id) : []; // Pais
            parente[3] = Array.isArray(parente[3]) ? parente[3].map(id => idParaNome[id] || id) : []; // Filhos
            parente[4] = Array.isArray(parente[4]) ? parente[4].map(id => idParaNome[id] || id) : []; // Irmãos
            parente[5] = idParaNome[parente[5]] || parente[5]; // Cônjuge
        });
    }

    carregarParentes();
});
