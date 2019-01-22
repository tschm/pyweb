lobnektable = {
    initColumns: function (columns, rend) {
        var cols = [];
        //rend = rend || (function(data, type, row, meta) {return data;});

        $.each(columns, function (i, val) {
            cols.push({"data": val, "render": rend(val), "defaultContent": "", "title": val});
        });

        return cols;
    },

    columns: function (fields) {
        var cols = [];
        $.each(fields, function (i, val) {
            cols.push(val.name);
        });
        return cols;
    },

    table: function(dom, frame, render) {
        console.log(frame);
        console.log(dom);
        columns = lobnektable.columns(frame.schema.fields);
        datarows = frame.data;

        console.log(columns);
        console.log(datarows);

        return $(dom).dataTable({
            data: frame.data,
            columns: lobnektable.initColumns(columns, render),
            scrollX: false,
            paging: false
        })
    },


}
