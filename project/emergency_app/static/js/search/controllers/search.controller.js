
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

	SearchController.$inject = ['$scope', '$rootScope', '$state', '$stateParams'];

	function SearchController($scope, $rootScope, $state, $stateParams){
		var vm = this;

		$scope.fname = '';
		$scope.lname = '';
		$scope.genders = ['M', 'F']
		$scope.gender = 'M';
		// $scope.buildings = [1,2,3,4]
		$scope.building = null;
		$scope.room = null;

		$scope.submit = function(){
			$scope.dataLoading = true;
			var resident = {}
			if ($scope.fname != ''){
				resident['fname'] = $scope.fname;
			}
			if ($scope.lname != ''){
				resident['lname'] = $scope.fname;
			}
			if($scope.gender != ''){
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