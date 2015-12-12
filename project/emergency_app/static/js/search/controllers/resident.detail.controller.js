
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

	ResidentDetailController.$inject = ['$scope', '$rootScope', '$state', '$stateParams'];

	function ResidentDetailController($scope, $rootScope, $state, $stateParams){
		var vm = this;
		$scope.residentDetail = findByKey($scope.residents, 'mrn', $stateParams.mrn)
		$rootScope.residentDetail = $scope.residentDetail
		console.log($scope.residentDetail)
		
		


		function findByKey(a, keyName, id){
			for(var i = 0; i < a.length; i++){
				if(a[i][keyName] == id){ return a[i]}
			}
			return null;
		}
	}
})();
