lobnekscreen = {
    navplot: function (name, series) {
        var table_mon = lobnekreport.monthTable("#tableMonth");
        var table_perf = lobnekreport.performanceTable("#tablePerformance");

        console.log(name);
        console.log(typeof series);
        console.log(series)

        var drawdown = lobnekperf.drawdown(series);
        var volatility = lobnekperf.volatility(series);
        var monthtable = lobnekperf.monthtable(series);

        $.when(drawdown, volatility, monthtable).then(function (drawdown, volatility, monthtable) {
            var xdrawdown = drawdown[0];
            var xvolatility = volatility[0];
            var xmonthtable = monthtable[0];

            console.log(xdrawdown);
            console.log(xvolatility);
            console.log(xmonthtable);

            console.log(typeof xmonthtable);

            table_mon.fnClearTable();
            table_mon.fnAddData(xmonthtable.data);

            var chart1 = $('#graph').highcharts('StockChart', {

                title: {
                    text: name
                },

                series: [
                    {
                        name: "NAV",
                        data: series,
                        type: "area",
                        fillColor: {
                            linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
                            stops: [
                                [0, Highcharts.getOptions().colors[0]],
                                [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                            ]
                        },
                        threshold: null,
                        yAxis: 0
                    },

                    {
                        name: "Drawdown",
                        data: xdrawdown,
                        yAxis: 1,
                        type: "area"
                    },

                    {
                        name: "Volatility",
                        data: xvolatility,
                        yAxis: 2,
                    }
                ],

                yAxis: [
                    {
                        labels: {color: 'blue'},
                        title: {
                            text: "Price", style: {color: 'blue'}
                        },
                        opposite: true,
                        height: '60%',
                        useUTC: false
                    },

                    {
                        labels: {color: 'blue'},
                        title: {
                            text: "Drawdown", style: {color: 'blue'}
                        },
                        opposite: true,
                        top: '60%',
                        height: '20%',
                        useUTC: false
                    },

                    {   // Secondary yAxis
                        labels: {color: 'red'},
                        title: {
                            text: "Volatility",
                            style: {color: 'red'}
                        },
                        top: '80%',
                        height: '20%',
                        offset: 0,
                        useUTC: false
                    }
                ],

                chart: {
                    events: {
                        load: function () {
                            lobnekperf.performance(this.series[0]).done(function (data) {
                                var rows = lobnekperf.parse(data);
                                table_perf.fnAddData(rows);
                            });
                        }
                    }
                },

                color: 'blue',
                rangeSelector: lobnekgraph.rangeselector,
                credits: {enabled: false},
                //credits: {href: "http://www.lobnek.com", text: "Lobnek Wealth Management"},

                tooltip: {valueDecimals: 2},
                useUTC: false,

                xAxis: {
                    events: {
                        afterSetExtremes: function () {
                            lobnekperf.performance(this.series[0]).done(function (data) {
                                var rows = lobnekperf.parse(data);
                                table_perf.fnClearTable();
                                table_perf.fnAddData(rows);
                            });

                        }
                    }
                },

                navigator: {
                    enabled: true,
                    series: {includeInCSVExport: false}
                },

                exporting: {
                    //showTable: true,
                    //tableCaption: 'Data table',
                    csv: {
                        /* // Uncomment for custom column header formatter.
                        // This function is called for each column header.
                        columnHeaderFormatter: function (item, key) {
                            if (!item || item instanceof Highcharts.Axis) {
                                return item.options.title.text;
                            }
                            // Item is not axis, now we are working with series.
                            // Key is the property on the series we show in this column.
                            return {
                                topLevelColumnTitle: 'Temperature',
                                columnTitle: key === 'y' ? 'avg' : key
                            };
                        },
                        // */
                        dateFormat: '%Y-%m-%d'
                    },
                    url: "lobnek.com"
                }

            });
        });
    }
};