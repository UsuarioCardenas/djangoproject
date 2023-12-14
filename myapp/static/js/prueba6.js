let dataTable;
let dataTableIsInitialised=false;

const initDataTable=async() => {
    if (dataTableIsInitialised) {
        dataTable.destroy();
    }
    await listGerundios();

    dataTable=$('#datatable-gerundios').dataTable({
        searching:false,
        paging:false,
        ordering:false,
        info: false,
        "scrollY": false,
        responsive:true,
        "scrollX": false,
        "columnDefs": [
            { "targets": [0], "visible": false }
        ]
    });
    dataTableIsInitialised=true;
};

const listGerundios= async () => {
    try {
        const response=await fetch("http://127.0.0.1:8000/list_gerundios/");
        const data=await response.json();

        let content=``;
        data.gerundios.forEach((gerundio,prueba6) => {
            content+=`
                <tr> 
                    <td>${prueba6}</td>
                    <td>${gerundio.verbo}</td>
                    <td>${gerundio.gerundio}</td>
                </tr>`;
        });
        tableBody_gerundios.innerHTML=content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
