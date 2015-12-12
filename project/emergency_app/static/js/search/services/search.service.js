/**
*Dashboard
*@namespace root.search.services
*/
(function(){
	'use strict';

	angular
		.module('root.search.services')
		.factory('Search', Search)

	Search.$inject = ['$http', '$rootScope', '$resource','$state', '$stateParams'];

	/**
	* @namespace search
	* @returns {Factory}
	*/
	function Search ($http, $rootScope, $resource, $state ,$stateParams) {
		var Search = {
			SearchResident: SearchResident,
			IncidentService: IncidentService,
			IncidentReprotService: IncidentReprotService,
			VitalSignsService: VitalSignsService,
		}

		return Search;

		function SearchResident(){
			console.log($rootScope.$stateParams)
			return $resource('/api/residents/', null, {
				'query': {method: 'GET', isArray:true},
			}).query($rootScope.$stateParams).$promise.then(function(data){
				return data
			});
		}

		function IncidentService(){
			return $resource('/api/incidents/', null, {
				'query': {method: 'GET', isArray:true},
				'update': {method: 'PUT', isArray:true},
				'post': {method: 'POST', isArray:false},
			});
		}

		function IncidentReprotService(){
			return $resource('/api/incidentReport/', null, {
				'query': {method: 'GET', isArray:true},
				'update': {method: 'PUT', isArray:true},
				'post': {method: 'POST', isArray:false},
			});
		}


		function VitalSignsService(){
			return $resource('/api/vitalsigns/', null, {
				'query': {method:'GET', isArray:true},
				'update': {method: 'PUT', isArray:true},
				'post': {method: 'POST', isArray:true},
			});
		}
	}

})();