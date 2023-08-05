
        driver.find_element_by_id("sf_submit").click()
        print('btn submit click')
        time.sleep(4)
        driver.find_element_by_class_name("def-btn-box").click()
        print('clicked')
        time.sleep(4)
        photo_path = glob.glob('/Users/aleksandramirnova/Downloads/*.mp4')
        downloaded_photo = photo_path[-1]
        print(downloaded_photo)
    except Exception as ex:
        print(ex)
get_video()
