/*global angular*/
'use strict';

var reportServices = angular.module('reportServices', ['ngResource']);

reportServices.factory('Report', ['$resource',
    function ($resource){
      return $resource('/api/reports/:reportId',
          {reportId: '@id'},
          {proposals: {method:'GET', params:{kind:0}, isArray:true},
            wishes: {method:'GET', params:{kind:1}, isArray:true},
            participations: {method:'GET', params:{kind:2}, isArray:true},
            questions: {method:'GET', params:{kind:3}, isArray:true}}
          );
    }
]);

reportServices.factory('ReportLoader', ['Report', '$route', '$q',
    function(Report, $route, $q){
      return function(){
        var delay = $q.defer();
        console.log('reportid');
        console.log($route.current.params.reportId);
        console.log(Report.get({reportId: 2}));
        // return Report.get({reportId: $route.current.params.reportId})
        Report.get(
            {reportId: $route.current.params.reportId},
            function(recipe){
              delay.resolve(recipe);
            },
            function(){
              delay.reject('Unable to fetch report' + $route.current.params.reportId);
            });
        return delay.promise;
      };
    }
]);

reportServices.service('loadGMapAPI', [
    '$window', '$q',
    function($window, $q){
      var defer = $q.defer();

      function loadScript(){
        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://maps.googleapis.com/maps/api/js?v=3.exp&' +
                     'callback=initGMapsAPI';
        document.body.appendChild(script);
      }

      $window.initGMapsAPI = function(){
        defer.resolve();
      };

      loadScript();

      return defer.promise;

    }
]);
