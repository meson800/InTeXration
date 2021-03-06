%include header base_url=base_url, title=identifier
%include navigation base_url=base_url, doc_link=''

<div class="container">
    <div class="row">
        <div class="col-md-9">
            % if len(errors) > 0:
            <div class="callout callout-error">
                <h1>Errors</h1>
                <div class="log">
                    % for line in errors:
                    {{line}} <br/>
                    % end
                </div>
            </div>
            % end
            % if len(warnings) > 0:
            <div class="callout callout-warning">
                <h1>Warnings</h1>
                <div class="log">
                    % for line in warnings:
                    {{line}} <br/>
                    % end
                </div>
            </div>
            % end
            <div id="all" class="callout callout-info">
                <h1>Log</h1>
                <div class="log">
                    % for line in all:
                    {{line}} <br/>
                    % end
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="panel panel-default">
                <div class="panel-heading"><span class="glyphicon glyphicon-file"></span> <b>Document</b></div>
                <table class="table">
                <tr>
                    <th>Errors</th>
                    <td>{{len(errors)}}</td>
                </tr>
                <tr>
                    <th>Warnings</th>
                    <td>{{len(warnings)}}</td>
                </tr>
                <tr>
                    <th>PDF</th>
                    <td><a href="{{base_url}}pdf/{{identifier.owner}}/{{identifier.repository}}/{{identifier.name}}">link</a></td>
                </tr>
                </table>
            </div>
        </div>
</div>

%include footer
