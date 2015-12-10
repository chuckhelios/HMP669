
/**
* ResidentController
* @namespace root.authentication.controllers
* @memberOf root.authentication
*/
(function () {
  'use strict';

  angular
    .module('root.search.controllers')
    .controller('ResidentController', ResidentController);

	ResidentController.$inject = ['$scope', '$rootScope', '$state', '$stateParams', 'residents'];

	function ResidentController($scope, $rootScope, $state, $stateParams, residents){
		var vm = this;
		$scope.residents = residents;
		console.log(residents)

	}
})();