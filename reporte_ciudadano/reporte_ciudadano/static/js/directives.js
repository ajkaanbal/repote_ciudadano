/*global google*/
'use strict';

var reportDirectives = angular.module('reportDirectives', []);

reportDirectives.directive('googleMap', [
  '$rootScope', 'loadGMapAPI',
  function($rootScope, loadGMapAPI){
    return {
      restrict: 'C',
      scope:{
        mapId: '@id',
        latitude: '@',
        longitude: '@'
      },
      link: function($scope, elem, attrs){
        if(angular.isDefined($scope.latitude) && angular.isDefined($scope.longitude)){
          $scope.initialize = function (){
            $scope.location = new google.maps.LatLng($scope.latitude, $scope.longitude);

            $scope.mapOptions = {
              zoom: 12,
              center: $scope.location
            };

            $scope.map = new google.maps.Map(document.getElementById($scope.mapId), $scope.mapOptions);

            new google.maps.Marker({
              position: $scope.location,
              map: $scope.map
            });
          }

          loadGMapAPI.then(
            function (){
              $scope.initialize();
            },
            function (){
              console.log('ok, somethings is wrong');
            }
          );
        }
      }
    }
  }
]);
