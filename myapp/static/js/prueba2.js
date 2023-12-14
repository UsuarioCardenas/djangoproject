let dataTable;
let dataTableIsInitialised=false;

const initDataTable=async() => {
    if (dataTableIsInitialised) {
        dataTable.destroy();
    }
    await listIrregulares();

    dataTable=$('#datatable-irregulares').dataTable({
        searching:false,
        paging:false,
        ordering:false,
        info: false,
        "scrollY": false,
        responsive:true,
        "scrollX": false,
        "columnDefs": [
            { "targets": [0,3], "visible": false }
        ]
    });
    dataTableIsInitialised=true;
};

const listIrregulares= async () => {
    try {
        const response=await fetch("http://127.0.0.1:8000/list_irregulares/");
        const data=await response.json();

        let content=``;
        data.irregulares.forEach((irregular,prueba2) => {
            content+=`
                <tr> 
                    <td>${prueba2}</td>
                    <td>${irregular.infinitivo}</td>
                    <td>${irregular.past}</td>
                    <td>${irregular.participe}</td>
                </tr>`;
        });
        tableBody_irregulares.innerHTML=content;
        
    } catch (ex) {
        alert(ex);
    }
};

window.addEventListener("load", async () => {
    await initDataTable();
});
