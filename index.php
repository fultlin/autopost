<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <?php
            echo htmlspecialchars($_POST['socset']);
            echo htmlspecialchars($_POST['token']);
            echo htmlspecialchars($_POST['content']);

            $data = array(
                'socset' => $_POST['socset'],
                'token' => $_POST['token'],
                'content' => htmlspecialchars($_POST['content']),
            );

            $json_data = json_encode($data);

            file_put_contents('data.json', $json_data);
        ?>
    <a href='index.html'>Назад</a>
</body>
</html>