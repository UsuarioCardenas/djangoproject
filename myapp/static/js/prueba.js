let dataTable;
let dataTableIsInitialised=false;

const initDataTable=async() => {
    if (dataTableIsInitialised) {
        dataTable.destroy();
    }
    await listVerbos();

    dataTable=$('#datatable-verbos').dataTable({
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

const listVerbos= async () => {
    try {
        const response=await fetch("http://127.0.0.1:8000/list_verbos/");
        const data=await response.json();

        let content=``;
        data.verbos.forEach((verbo,prueba) => {
            content+=`
                <tr> 
                    <td>${prueba}</td>
                    <td>${verbo.infinitivo}</td>
                    <td>${verbo.past}</td>
                    <td>${verbo.participe}</td>
                </tr>`;
        });
        tableBody_verbos.innerHTML=content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
