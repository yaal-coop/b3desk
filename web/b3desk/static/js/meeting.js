// ALL FUNCTIONS FOR JS, NO EXECUTION HAPPNING RIGHT THERE, JUMP TO 'STARTJSEXEC' IF YOU WISH TO SEE JSS CODE EXECUTION

function changeDefaultFile(newId){
    let tbody=document.getElementById('fileslist');
    let actualDefaultFile = tbody.querySelector('[disabled]');
    if (actualDefaultFile) {
        actualDefaultFile.checked=false;
        actualDefaultFile.disabled=false;
    }
    let newDefault = document.getElementById('isDefault-'+newId);
    newDefault.checked=true;
    newDefault.disabled=true;

}

function toggleIsDownloadable(e){
    let idFileSelected = e.target.id.split('-')[1];
    let newValue = e.target.checked;
    let csrf_token = document.getElementsByName("csrf_token")[0].value;

    fetch(toggle_download_url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken':csrf_token
        },
        body: JSON.stringify({'id': idFileSelected, 'value': newValue})
    })
    .then(res => res.json())
    .then(res => {
        //printout_message({ type: 'success', title: 'Modification prise en compte' });
    })
}

function submitDefaultFile(e){
    let csrf_token = document.getElementsByName("csrf_token")[0].value;
    let idFileSelected = e.target.id.split('-').slice(-1);

    fetch(set_default_file_url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken':csrf_token
        },
        body: JSON.stringify({'id': idFileSelected})
    })
    .then(res => res.json())
    .then(res => {
        changeDefaultFile(res.id);
    })
}

function remove_file_from_fileslist(id){
    let liToDel = document.getElementById(id);
    liToDel.parentNode.removeChild(liToDel);
}

function deleteFile(e){
    e.preventDefault();

    let csrf_token = document.getElementsByName("csrf_token")[0].value;
    let idFileSelected = e.target[0].value;
    fetch(delete_meeting_file_url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken':csrf_token
        },
        body: JSON.stringify({'id': idFileSelected})
    })
    .then(res => res.json())
    .then(res => {
        close_dialog('delete-file-'+res.id);
        remove_file_from_fileslist(res.id);
        printout_message({ type: 'success', title: 'Document supprimé', data: res.msg});
        if (res.newDefaultId) {
            changeDefaultFile(res.newDefaultId);
        }
    })
}

function add_URL_file(name, from) {

    //on teste que l'URL est pas trop exotique
    if (! name.match(/(http(s)?:\/\/.)?([-a-zA-Z0-9@:%._\+~#=]{2,256}\.){1,10}[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g)) {
        alert('URL mal formattée elle doit être de la forme ( [] = optionnel ): http[s]://[www.]monsite.fr/[mon-chemin]');
        return ;
    }
    // si pas de https:// renseigné, on le force en préfixe, si c'est du http, la personne    devra corriger d'elle-même
    if (!name.match(/^http/)) {
        name = `https://${name}`;
    }
    link_file_to_meeting(name, 'URL');

}

function append_file_to_fileslist(title, id, date, isDefault) {
    var nofileavailable = document.getElementById('nofileavailable');
    if (nofileavailable) {
        nofileavailable.parentNode.removeChild(nofileavailable);
    }
    var csrf_token = document.getElementsByName("csrf_token")[0].value;
    var tbody = document.getElementById("fileslist");

    // create TR-TD element
    let tr = document.createElement('tr');
    let tdDefault = document.createElement('td');
    let inputDefault = document.createElement('input');
    let labelDefault = document.createElement('label');
    let divDefault = document.createElement('div');
    let tdTitle = document.createElement('td');
    let tdDate = document.createElement('td');
    let tdDel = document.createElement('td');
    let tdDownload = document.createElement('td');
    let tdIsDownloadable = document.createElement('td');
    let divLink = document.createElement('div');
    let divIsDl = document.createElement('div');
    let inputIsDl = document.createElement('input');
    let labelIsDl = document.createElement('label');
    let aLink = document.createElement('a');
    let buttonLink = document.createElement('button');
    let deleteButton = document.createElement('button');

    tr.setAttribute('id', id);
    deleteButton.setAttribute('data-fr-opened', 'false');
    deleteButton.setAttribute('title', 'Supprimer');
    deleteButton.classList.add('fr-btn','fr-fi-delete-line');

    buttonLink.classList.add('fr-btn','fr-icon-download-fill');
    buttonLink.setAttribute('title', 'Télécharger');
    aLink.setAttribute('href', download_meeting_file_url + id);
    aLink.appendChild(buttonLink);
    tdDownload.appendChild(aLink);
    inputIsDl.classList.add('fr-toggle__input');
    inputIsDl.setAttribute('id', 'toggle-'+id);
    inputIsDl.setAttribute('type', 'checkbox');
    inputIsDl.addEventListener('click', toggleIsDownloadable);
    labelIsDl.classList.add('fr-toggle__label');
    labelIsDl.setAttribute('for', 'toggle-'+id);
    labelIsDl.setAttribute('data-fr-checked-label', 'Oui');
    labelIsDl.setAttribute('data-fr-unchecked-label', 'Non');

    divIsDl.classList.add('fr-toggle');
    divIsDl.appendChild(inputIsDl);
    divIsDl.appendChild(labelIsDl);
    tdIsDownloadable.appendChild(divIsDl);
    tdTitle.innerHTML=title;
    tdDate.innerHTML=date;

    inputDefault.classList.add('fr-toggle__input');
    inputDefault.setAttribute('id', 'isDefault-'+id);
    inputDefault.setAttribute('type', 'checkbox');
    inputDefault.addEventListener('click', submitDefaultFile);
    if (isDefault) {
        inputDefault.setAttribute('checked', true);
        inputDefault.disabled=true;
    }
    labelDefault.classList.add('fr-toggle__label');
    labelDefault.setAttribute('data-fr-checked-label', 'Oui');
    labelDefault.setAttribute('data-fr-unchecked-label', 'Non');
    labelDefault.setAttribute('for', 'isDefault-'+id);
    divDefault.classList.add('fr-toggle');
    divDefault.appendChild(inputDefault);
    divDefault.appendChild(labelDefault);
    tdDefault.appendChild(divDefault);


    tr.appendChild(tdDefault);
    tr.appendChild(tdIsDownloadable);
    tr.appendChild(tdTitle);
    tr.appendChild(tdDate);
    tr.appendChild(tdDel);
    tr.appendChild(tdDownload);

    // create delete element - modal
    let dialog = document.createElement('dialog');
    let div1 = document.createElement('div');
    let div2 = document.createElement('div');
    let div3 = document.createElement('div');
    let div4 = document.createElement('div');
    let div5a = document.createElement('div');
    let div5b = document.createElement('div');
    let button = document.createElement('button');
    let button2 = document.createElement('button');
    let button3 = document.createElement('button');
    let form = document.createElement('form');
    let input = document.createElement('input');
    let p = document.createElement('p');

    let modalId = 'delete-file-'+id

    deleteButton.setAttribute('aria-controls', modalId);

    dialog.setAttribute('id', modalId);
    dialog.classList.add('fr-modal');
    div1.classList.add('fr-container','fr-container--fluid','fr-container-md');
    div2.classList.add('fr-grid-row','fr-grid-row--center');
    div3.classList.add('fr-col-12','fr-col-md','fr-col-lg-6');
    div4.classList.add('fr-modal__body');
    div5a.classList.add('fr-modal__header');
    div5b.classList.add('fr-modal__content');
    button.classList.add('fr-btn--close','fr-btn');
    button.setAttribute('title', 'Fermer');
    button.setAttribute('aria-controls', modalId);

    button2.setAttribute('type', 'submit');
    button2.classList.add('fr-btn','fr-btn--primary');
    button2.innerHTML = 'Supprimer';
    button3.setAttribute('type', 'reset');
    button3.setAttribute('aria-controls', modalId);
    button3.classList.add('fr-btn','fr-btn--secondary');
    button3.innerHTML = 'Annuler';
    input.classList.add('fr-input');
    input.setAttribute('type', 'hidden');
    input.setAttribute('name', 'id');
    input.setAttribute('value', id);
    form.setAttribute('action', delete_meeting_file_url);
    form.setAttribute('method', 'POST');
    form.setAttribute('onsubmit', 'deleteFile(event)');


    form.appendChild(input);
    form.appendChild(button2);
    form.appendChild(button3);

    div5a.appendChild(button);
    p.innerHTML = 'Voulez-vous vraiment supprimer le fichier '+title+' ?';
    div5b.appendChild(p);
    div5b.appendChild(form);
    div4.appendChild(div5a);
    div4.appendChild(div5b);
    div3.appendChild(div4);
    div2.appendChild(div3);
    div1.appendChild(div2);
    dialog.appendChild(div1);

    tdDel.appendChild(deleteButton);
    tbody.appendChild(dialog);
    tbody.appendChild(tr);
}

//
    // msg should be formatted :
// {
    //    type : success/fail
    //    title :
    //    data :
    // }
//
function printout_message(msg){
    let div=document.createElement('div');
    let h3=document.createElement('h3');
    let p=document.createElement('p');
    div.classList.add('fr-alert','fr-alert--'+msg.type);
    h3.classList.add('fr-alert__title');
    h3.innerHTML=msg.title;
    p.innerHTML=msg.data;

    div.appendChild(h3);
    div.appendChild(p);

    nodeToPrepend = document.getElementById('layoutContainer');
    parentNodeToPrepend = nodeToPrepend.parentNode;
    parentNodeToPrepend.insertBefore(div, nodeToPrepend);
    window.scrollTo(0, 0);
    setTimeout(() => {
        parentNodeToPrepend.removeChild(div);
    }, 3000)
}

function close_dialog(id){
    let dialogToClose = document.getElementById(id);
    dsfr(dialogToClose).modal.conceal();
}

// post data as :
// [
    // { 'from' : 'URL', 'value': 'https://lol.com/image.jpg' },
    // { 'from' : 'dropzone', 'value': 'tancarville.jpeg' },
    // ]

function link_file_to_meeting(value, from) {
    var csrf_token = document.getElementsByName("csrf_token")[0].value
    var post_data = {
        'value': value,
        'from': from,
    };
    JSON.stringify(post_data);
    fetch(add_meeting_files_url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken':csrf_token
        },
        body: JSON.stringify(post_data)
    })
    .then(res => {
        if (res.status == 200) {
            return (res.json())
        } else {
            throw res
        }

    })
    .then(data => {
        if (data.status == 200) {
            append_file_to_fileslist(data.title, data.id, data.created_at, data.isDefault);
            printout_message({ type: 'success', title: 'Document ajouté', data: 'Le document '+data.title+' a bien été ajouté'});
            if (data.isfrom !== 'nextcloud') {
                close_dialog(data.isfrom);
            }
        } else {
            throw data
        }
    })
    .catch(data => {
        console.log(data)
        printout_message({ type: 'error', title: 'Erreur Document', data: data.msg});
        if (data.isfrom !== 'nextcloud') {
            close_dialog(data.isfrom);
        }
    })
}

function openNCFilePicker(e) {
    ncfilepicker.getFilesPath();
}


function createNCFilePicker() {
    let ncPickerParams = {
        url: nc_locator,
        login: nc_login,
        accessToken: nc_token,
        enableGetFilesPath: true,
    };

    ncfilepicker = window.createFilePicker('ncfilepicker', ncPickerParams);
    document.addEventListener('get-files-path', (e) => {
        //    { selection: [ 'lol.jpg', 'megalol.jpg' ] }
        e.detail.selection.map( (name, index) => {
            setTimeout(() => {link_file_to_meeting(name.slice(1), 'nextcloud')}, index * 500);
        })

    })
}

// END OF JS FUNCTION DECLARATION
// HERE IS STARTJSEXEC

let ncfilepicker = null;

document.addEventListener('DOMContentLoaded', () => {

    if (!nc_locator || !nc_login || !nc_token) {
        printout_message({ type: 'error', title: 'Nextcloud connexion', data: "La connexion avec votre Nextcloud n'est pas fonctionnelle, les options associées sont désactivées"});
    }

    Dropzone.autoDiscover = false;
    var dropzone_conf = {
        paramName: 'dropzoneFiles',
        //autoProcessQueue: false,
        //uploadMultiple: true,
        //chunking: false,
        //forceChunking: false,
        chunking: true,
        forceChunking: true,
        maxFilesize: 20, // megabytes
        acceptedFiles: accepted_files,
        dictRemoveFile: 'Supprimer',
        dictDefaultMessage: 'Cliquer ou glisser-déposer les fichiers à ajouter',
        addRemoveLinks: true,
        parallelUploads: 10,
        chunkSize: 1000000, // bytes
        init: function() {
            this.on("removedfile", file => {
                console.log('removed file from dropzone');
            });
            this.on('success', file => {
                setTimeout(() => {link_file_to_meeting(file.name, 'dropzone')}, this.getUploadingFiles().length * 1000);
                setTimeout(() => {this.removeFile(file)}, 1000);
            });
            this.on('error', (file, message) => {
                close_dialog('dropzone');
                printout_message({ type: 'error', title: 'Le téléversement du fichier « '+file.name+' » a échoué.', data: message});
                this.removeFile(file);
            });
        }
    }
    var dropper = new Dropzone("form#dropper", dropzone_conf);

    var form_files = document.getElementById('meeting-form');

    form_files.addEventListener('submit', (e) => {
        e.preventDefault();

        var formData = new FormData(form_files);

        var name = `${formData.get('url')}`;
        var from = `depuis URL`;

        add_URL_file(name, from);
    });

    createNCFilePicker()
})
