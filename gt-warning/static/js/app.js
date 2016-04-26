var App = angular
    .module('gtWarning', [
        'ui.router'
    ]).config(function ($locationProvider, $stateProvider, $urlRouterProvider, $sceDelegateProvider) {
        $sceDelegateProvider.resourceUrlWhitelist([
            'self'
        ]);

        $stateProvider.state('channel', {
            url: "/",
            templateUrl: "/static/templates/channel.html",
            controller: "ChannelCtrl",
            displayName: "Channel"
        }).state('member', {
            url: "/members",
            templateUrl: "/static/templates/members.html",
            controller: "MemberCtrl",
            displayName: "Member"
        }).state('groups',{
            url: "/groups",
            templateUrl: "/static/templates/groups.html",
            controller: "GroupCtrl"
        }).state('logs', {
            url: "/logs",
            templateUrl: "/static/templates/logs.html",
            controller: "LogCtrl",
            displayName: "Logs"
        });

        $urlRouterProvider.otherwise('/');
        $locationProvider.html5Mode(true);
    }).run(function ($rootScope) {
        $rootScope.$on('$stateChangeSuccess',
            function (event, toState) {
                $rootScope.title = toState.displayName;
                event.preventDefault();
            });
    });
