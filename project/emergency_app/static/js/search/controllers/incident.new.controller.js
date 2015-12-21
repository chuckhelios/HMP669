
/**
* IncidentNewController
* @namespace root.authentication.controllers
* @memberOf root.authentication
*/
(function () {
  'use strict';

  angular
    .module('root.search.controllers')
    .controller('IncidentNewController', IncidentNewController);

	IncidentNewController.$inject = ['$scope', '$rootScope', '$state', '$stateParams', 'Search', 'Snackbar'];

	function IncidentNewController($scope, $rootScope, $state, $stateParams, Search, Snackbar){
		var vm = this;
		// $scope.residentDetail= $rootScope.residentDetail
		$scope.newIncident = {
			eventid: null,
			empid: $rootScope.globals.currentUser.username,
			mrn: $scope.residentDetail.mrn,
			startdatetime: null,
			enddatetime: null,
			narrative: '',
			hospitalid: ''
		};
		var latestEventID = null;
		Search.IncidentService().query({'last':1}).$promise.then(function(data){
			latestEventID = data[0]['eventid'];
			console.log(latestEventID)
			$scope.newIncident.eventid = latestEventID+1
		});
		var vitalID = null;
		Search.VitalSignsService().query({'last':1}).$promise.then(function(data){
			vitalID = data[0]['uniqueid'];
			console.log(vitalID)

		});

		$scope.newVitals = [];

		
		$scope.submit = function(){
			console.log($scope.newVitals);
			Search.IncidentService().post($scope.newIncident).$promise.then(postSuccessFn, postErrorFn);
			Search.VitalSignsService().post($scope.newVitals).$promise.then(postSuccessFn, postErrorFn);

		}

		$scope.addVital = function(){
			vitalID+=1;
			$scope.newVitals.push({
				'uniqueid': vitalID,
				'eventid': latestEventID,
				'empid': null,
				'assesmdatetime': '',
				'vitaltype': '',
				'results': '',
				'comments': '',
			});
		}

		$scope.removeVital = function(index){
			$scope.newVitals.splice(index,1);
		}

    	/**
	    * @name postSuccessFn
	    * @desc visual cue for post successfully
	    * @memberOf root.search.controllers.IncidentNewController
	    */
	    function postSuccessFn(data, status, headers, config){
			$scope.dataLoading = false;
			// change GUI variables
	    	console.log("post good");
	    	Snackbar.show('Success! Post Created.');
	    }		


    	/**
	    * @name postErrorFn
	    * @desc visual cue for post error
	    * @memberOf root.search.controllers.IncidentNewController
	    */
	    function postErrorFn(data, status, headers, config){
	    	$rootScope.$broadcast('post.created.error');
	    	console.log(data);
	    	Snackbar.error(data.statusText);
	    }	


	}
})();
