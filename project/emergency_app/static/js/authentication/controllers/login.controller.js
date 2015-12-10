/**
* LoginController
* @namespace root.authentication.controllers
* @memberOf root.authentication
*/
(function () {
  'use strict';

  angular
    .module('root.authentication.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$state', '$scope', '$rootScope', '$cookies', '$timeout', 'Authentication'];
  /**
  * @name LoginController
  * @namespace root.authentication.controllers.LoginController
  * @memberOf root.authentication.controllers
  */
  function LoginController($state, $scope, $rootScope, $cookies, $timeout, Authentication) {
    var vm = this;
    $scope.submitBtn = "Submit";
    vm.login = login;
    $scope.IsLoginError = false;
    $scope.ErrorMsg = '';
    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf root.authentication.controllers.LoginController
    */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        // $state.go('home');
        window.location = '/';
      }
    }


    /**
    * @name login
    * @desc Log the user in
    * @memberOf root.authentication.controllers.LoginController
    */
    function login() {
      $scope.dataLoading = true;

      Authentication.login($scope.username, $scope.password, function(response){        
        if(response.status==401){
          console.log(response.data.message);
          $scope.loginError = response.data.message;
          $scope.dataLoading = false;          
        }else{
          $scope.dataLoading = false;
          $timeout(activate());          
        }
      });
    }
    // end login


  }
})();