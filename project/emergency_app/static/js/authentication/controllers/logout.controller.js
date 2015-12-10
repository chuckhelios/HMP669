/**
* LogoutController
* @namespace root.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('root.authentication.controllers')
    .controller('LogoutController', LogoutController);

  LogoutController.$inject = ['$scope', 'Authentication'];

  /**
  * @namespace LogoutController
  */
  function LogoutController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    /**
    * @name logout
    * @desc Log the user out
    * @memberOf root.authentication.controllers.LogoutController
    */
    function logout() {
      $scope.processLogout = true;
      Authentication.logout(function(response){
        $scope.processLogout = false;
      });
    }
  }
})();
