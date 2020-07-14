const performance = {
    parse: function (x) {
        rows = [];
        for (var key in x) {
            rows.push({"name": key, "value": x[key]});
        }
        return rows;
    },

    truncate: function (s) {
        var n = s.xData.length;
        var pairs = [];

        for (i = 0; i < n; i++) {
            if (s.xData[i] >= s.xAxis.getExtremes().min && s.xData[i] <= s.xAxis.getExtremes().max) {
                pairs.push([s.xData[i], s.yData[i]])
            }
        }

        return pairs;
    },

    performance: function (s) {
        console.log("{{ url_for('engine', filename='performance') }}");
        return $.ajax({
            url: "{{ url_for('post.static', filename='performance') }}",
            type: "POST",
            data: JSON.stringify(performance.truncate(s)),
            contentType: "application/json; charset=utf-8"
        });
    },


    monthtable: function (s) {
        console.log("{{ url_for('engine', filename='monthtable') }}");
        return $.ajax({
            url: "{{ url_for('engine', filename='month') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8"
        });
    },

    drawdown: function (s) {
        console.log("{{ url_for('engine', filename='drawdown') }}");
        return $.ajax({
            url: "{{ url_for('engine', filename='drawdown') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8",
        });
    },

    volatility: function (s) {
        console.log("{{ url_for('engine', filename='volatility') }}");
        return $.ajax({
            url: "{{ url_for('engine', filename='volatility') }}",
            type: "POST",
            data: JSON.stringify(s),
            contentType: "application/json; charset=utf-8",
        });
    }
};
