const lobnekreport = {
    render: function (column) {
        return function (data, type, row, meta) {
            return data;
        }
    },

    performanceTable: function (dom) {
        const header = ["name", "value"];

        return $(dom).dataTable({
            scrollX: false,
            paging: false,
            columns: lobnektable.initColumns(header, lobnekreport.render),
            bFilter: false,
            info: false,
            bSort: false
        });
    },

    monthTable: function (dom) {
        const header = ["Year", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "STDev", "YTD"];

        return $(dom).dataTable({
            columns: lobnektable.initColumns(header, lobnekreport.render),
            scrollX: false,
            bFilter: false,
            paging: false,
            info: false,
            bSort: false,
            order: [[0, "desc"]]
        })
    },
};
