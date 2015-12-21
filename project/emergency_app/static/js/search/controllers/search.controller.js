
/**
* LoginController
* @namespace root.authentication.controllers
* @memberOf root.authentication
*/
(function () {
  'use strict';

  angular
    .module('root.search.controllers')
    .controller('SearchController', SearchController);

	SearchController.$inject = ['$scope', '$rootScope', '$state', '$stateParams', 'Buildings'];

	function SearchController($scope, $rootScope, $state, $stateParams, Buildings){
		var vm = this;

		$scope.fname = '';
		$scope.lname = '';
		$scope.genders = ['M', 'F'];
		$scope.gender = 'All';
		$scope.buildings = Buildings;
		$rootScope.buildings = $scope.buildings;
		$scope.building = null;
		$scope.room = null;

		// console.log($scope.buildings);

		$scope.submit = function(){
			$scope.dataLoading = true;
			var resident = {}
			if ($scope.fname != ''){
				resident['fname'] = $scope.fname;
			}
			if ($scope.lname != ''){
				resident['lname'] = $scope.fname;
			}
			if($scope.gender != '' && $scope.gender!='All'){
				resident['gender'] = $scope.gender;
			}
			if($scope.building != null){
				resident['building'] = $scope.building;
			}
			if($scope.room != null) {
				resident['room'] = $scope.room;
			}

			$rootScope.$stateParams = resident

			$state.go('resident.list');

		}


	}
})();