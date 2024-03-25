<?php
    if (isset($_FILES['image']) && isset($_POST['content'])) {
        $myimg = './uploads/' . basename($_FILES['image']['name']);
        move_uploaded_file($_FILES['image']['tmp_name'], $myimg);
    
        if (isset($_POST['tg']) && isset($_POST['vk'])) {
            $data = array(
                'content' => htmlspecialchars($_POST['content']),
                'tg-channel' => $_POST['tg-channel'],
                'access-token-vk' => $_POST['access-token-vk'],
                'vk-id' => $_POST['vk-id'],
                'img' => $myimg,
            );

            $json_data = json_encode($data);

            file_put_contents('data.json', $json_data);

            $test = shell_exec('python send.py');
            $test_vk = shell_exec('python send_vk.py');
        } elseif (isset($_POST['tg']) && !isset($_POST['vk'])) {
            $data = array(
                'content' => htmlspecialchars($_POST['content']),
                'tg-channel' => $_POST['tg-channel'],
                'img' => $myimg,
            );

            $json_data = json_encode($data);

            file_put_contents('data.json', $json_data);

            $test = shell_exec('python send.py');
        } elseif (!isset($_POST['tg']) && isset($_POST['vk'])) {
            $data = array(
                'content' => htmlspecialchars($_POST['content']),
                'access-token-vk' => $_POST['access-token-vk'],
                'vk-id' => $_POST['vk-id'],
                'img' => $myimg,
            );

            $json_data = json_encode($data);

            file_put_contents('data.json', $json_data);
            $test = shell_exec('python send_vk.py');
        }
    }
    header('Location: ' . $_SERVER['HTTP_REFERER']);      
?>
