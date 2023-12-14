let dataTable;
let dataTableIsInitialised=false;

const initDataTable=async() => {
    if (dataTableIsInitialised) {
        dataTable.destroy();
    }
    await listAdjetivos();

    dataTable=$('#datatable-adjetivos').dataTable({
        searching:false,
        paging:false,
        ordering:false,
        info: false,
        "scrollY": false,
        responsive:true,
        "scrollX": false,
        "columnDefs": [
            { "targets": [0,2], "visible": false }
        ]
    });
    dataTableIsInitialised=true;
};

const listAdjetivos= async () => {
    try {
        const response=await fetch("http://127.0.0.1:8000/list_adjetivos/");
        const data=await response.json();

        let content=``;
        data.adjetivos.forEach((adjetivo,prueba3) => {
            content+=`
                <tr> 
                    <td>${prueba3}</td>
                    <td>${adjetivo.adjetivo}</td>
                    <td>${adjetivo.comparativo}</td>
                    <td>${adjetivo.superlativo}</td>
                </tr>`;
        });
        tableBody_adjetivos.innerHTML=content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
