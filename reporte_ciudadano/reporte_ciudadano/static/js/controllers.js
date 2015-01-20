'use strict';

var reportControllers = angular.module('reportControllers', []);

reportControllers.controller('HomeController', [
  '$scope', 'Report', '$location',
  function ($scope, Report, $location){
    $scope.reports = Report.query();
    $scope.proposals = Report.proposals();
    $scope.wishes = Report.wishes();
    $scope.participations = Report.participations();
    $scope.questions = Report.questions();
    $scope.showReport = function(report){
      $location.path('/detalle-reporte/' + report.id);
    };
  }
]);

reportControllers.controller('ReportController', [
  '$scope', 'Report',
  function ($scope, Report){
    $scope.report = {};
    $scope.save = function (){
      Report.save({}, $scope.report);
    };
  }
]);

reportControllers.controller('ReportListController', [
  '$scope', 'Report', '$location',
  function ($scope, Report, $location){
    $scope.reports = Report.query();
    $scope.showReport = function(report){
      $location.path('/detalle-reporte/' + report.id);
    };
  }
]);

reportControllers.controller('ReportDetailsController', [
  '$scope', 'report',
  function ($scope, report){
    $scope.report = report;
  }
]);
