/*global angular */
'use strict';

var reportApp = angular.module('reportApp', [
  'ngRoute',
  'ngCookies',
  'reportControllers',
  'reportServices'
]);

reportApp.config(['$routeProvider',
  function($routeProvider) {
    // $httpProvider.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    // console.log($cookies);

    $routeProvider.
      when('/', {
        templateUrl: 'partials/home.html',
        controller: 'HomeController'
      }).
      when('/nueva-propuesta', {
        templateUrl: 'partials/new_report.html',
        controller: 'ReportController'
      }).
      when('/nueva-pregunta', {
        templateUrl: 'partials/new_report.html',
        controller: 'ReportController'
      }).
      when('/listado-de-participaciones', {
        templateUrl: 'partials/report_list.html',
        controller: 'ReportListController'
      }).
      when('/detalle-reporte/:reportId', {
        templateUrl: 'partials/report_details.html',
        controller: 'ReportDetailsController',
        resolve: {
          report: function(ReportLoader){
            return ReportLoader();
          }
        }
      }).
      otherwise({
        redirectTo: '/'
      });
  }
]);

reportApp.run(
  function ($http, $cookies){
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
  }
);

