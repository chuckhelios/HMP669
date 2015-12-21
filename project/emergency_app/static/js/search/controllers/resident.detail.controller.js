
/**
* ResidentDetailController
* @namespace root.authentication.controllers
* @memberOf root.authentication
*/
(function () {
  'use strict';

  angular
    .module('root.search.controllers')
    .controller('ResidentDetailController', ResidentDetailController);

	ResidentDetailController.$inject = ['$scope', '$rootScope', '$state', '$stateParams', 'Hospitals'];

	function ResidentDetailController($scope, $rootScope, $state, $stateParams, Hospitals){
		var vm = this;
		$scope.residentDetail = findByKey($scope.residents, 'mrn', $stateParams.mrn);
		$rootScope.residentDetail = $scope.residentDetail;
		// $scope.buildings = $rootScope.buildings;
		$scope.hospitals = Hospitals;
		console.log($rootScope.globals.currentUser.username);

		function findByKey(a, keyName, id){
			for(var i = 0; i < a.length; i++){
				if(a[i][keyName] == id){ return a[i];}
			}
			return null;
		}
	}
})();
