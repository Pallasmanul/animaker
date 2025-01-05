;;;###autoload
(defun eaf-open-animaker ()
  "Open EAF demo screen to verify that EAF is working properly."
  (interactive)
  (eaf-open "eaf-aniamker" "animaker"))

(setq eaf-animaker-module-path (concat (file-name-directory load-file-name) "buffer.py"))
(add-to-list 'eaf-app-module-path-alist '("animaker" . eaf-animaker-module-path))

(provide 'eaf-animaker)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; animaker.el ends here
